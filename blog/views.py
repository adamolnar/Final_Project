from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category, Tag
from author.models import Author
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# Generic class-based view for a list of all posts.
class PostListView(ListView): 
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        queryset = Post.objects.filter(status=1).order_by("-created_on")
        category_id = self.request.GET.get('category_id')
        tag = self.request.GET.get('tag')

        if category_id:
            queryset = queryset.filter(categories__id=category_id)

        if tag:
            queryset = queryset.filter(tags__name__icontains=tag)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


# Generic class-based detail view for a post.
class PostDetailView(DetailView):   
    def get(self, request, slug, *args, **kwargs):
        # Retrieve the post and associated data
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm()
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Render the post detail page with relevant data
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        # Handle comment submission
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset,slug=slug)
        form = CommentForm(request.POST)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            form = CommentForm()           
        else:
            form = CommentForm()

        # Render the post detail page with updated data
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "approved":True,
                "commented": True,
                "form": form,
                "liked": liked
            },
        )


# Generic class-based view for a like/unlike.
class PostLikeView(LoginRequiredMixin, View): 
    def post(self, request, slug, *args, **kwargs):
        # Handle post liking/unliking
        post = get_object_or_404(Post,  slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post-detail', args=[slug]))

def is_author(user):
    return user.groups.filter(name='author').exists()

# Generic class-based view to create new post.
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):  
    model = Post
    fields = ["title", "content", "image", 'status', 'categories',"tags"]
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # Save the new post and associated data
        messages.success(self.request, 'Your post has been created successfully.')
        
        # Set the author and slug before saving
        form.instance.author = Author.objects.get(profile=self.request.user.profile)
        form.instance.slug = slugify(form.cleaned_data['title'])

        # Save the form and get the object
        self.object = form.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # Check if the object has been created and has a status attribute
        if self.object and hasattr(self.object, 'status'):
            # Check the status of the created post
            if self.object.status == 1:  # Assuming 1 represents a published post
                return reverse_lazy('post-detail', kwargs={'slug': self.object.slug})
            elif self.object.status == 0:  # Assuming 0 represents a draft post
                return reverse_lazy('draft-post-author-list')

        # Default to index if the status is neither 0 nor 1
        return reverse_lazy('index')

    
    def test_func(self):
        # Check if the user is associated with an Author model
        return Author.objects.filter(profile=self.request.user.profile).exists()
    
    def handle_no_permission(self):
        # Handle the case where the user doesn't pass the test
        messages.warning(self.request, 'You are not authorized to create a post.')
        return redirect('request-author-access')  # Redirect to the request author access page


# Generic class-based view to update post only by the author of the post.       
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content", "image"]
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        slug = self.kwargs['slug']
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy('post-detail', kwargs={'slug': slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Ensure that the user is the author of the post
        if obj.author.id != self.request.user.pk:
            print(obj.author.id , self.request.user.pk )
            raise PermissionError("You are not authorized to update this post.")
        return obj
    

class PublishPostView(View):
    def post(self, request, slug, *args, **kwargs):
        # Retrieve the post object
        post = get_object_or_404(Post, slug=slug)

        # Check if the user has permission to publish (e.g., is the post's author)
        if request.user.profile != post.author.profile:
            # You may want to handle unauthorized access differently, e.g., show an error message
            messages.error(request, 'You do not have permission to publish this post.')
            return redirect('post-detail', slug=slug)

        # Update the post's status to 1 (published)
        post.status = 1
        post.save()

        # Add a success message
        messages.success(request, 'The post has been published successfully.')

        # Redirect to the post detail page
        return redirect('index')


# Generic class-based view to delete post.
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('index')

    def get(self, request, slug, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, slug, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, 'The post has been deleted successfully.')
        return super().post(request, *args, **kwargs)
    
@method_decorator(login_required, name='dispatch')
class DraftPostAuthorListView(ListView):
    model = Post
    template_name = "blog/draft_post_author.html"  # Create a template for displaying draft posts by a particular author
    context_object_name = 'draft_post_list'
    paginate_by = 5

    def get_queryset(self):
        # Filter draft posts for the currently logged-in author
        return Post.objects.filter(author=self.request.user.profile.id, status=0).order_by("-created_on")
    

# Generic class-based view for author update comment function.
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['body'] 
    template_name = 'blog/comment_update.html' 

    def form_valid(self, form):
        # Save the updated comment
        form.save()
        messages.success(self.request, "Comment Updated Successfully!!")
        return HttpResponseRedirect(reverse('index'))
    

# Generic class-based view for author delete comment function.
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html' 

    def get(self, request, pk, *args, **kwargs):
        # Retrieve and render the comment for deletion
        comment = get_object_or_404(Comment, pk=pk)
        context = {'comment': comment}
        if request.method == 'GET':
            return render(request, 'blog/comment_delete.html',context)

    def post(self, request, pk, *args, **kwargs):
        # Handle comment deletion
        comment = get_object_or_404(Comment, pk=pk)    
        if request.method == 'POST':
            comment.delete()
            messages.success(request, 'The comment has been deleted successfully.')
        return HttpResponseRedirect(reverse('index'))
    

# Function that will be called when a 404 error occurs
def custom_404(request, exception):
    """
    Custom 404 error view.
    """
    return render(request, 'blog/404.html', {'exception': exception}, status=404)


def byte_by_byte_view(request):
    # Define a view function for rendering the "byte_by_byte.html" template.
    
    # Optionally, you can prepare context data to pass to the template.
    context = {
        'page_title': 'Byte by Byte Tech Blog',  # Example: Set the page title.
        'blog_content': 'Welcome to the Byte by Byte Tech Blog!',  # Example: Add some content.
    }
    
    # Render the "byte_by_byte.html" template with the provided context data.
    return render(request, 'blog/byte_by_byte.html', context)
