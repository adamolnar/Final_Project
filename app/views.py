from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post, Author, Profile, Comment
from .forms import CommentForm, ContactForm
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# Generic class-based view to display user profile details.
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'app/profile.html'
   
    
# Generic class-based view to update logged-in user profile.
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["about_me", 'image']


# Generic class-based view to delete user profile. 
class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'app/profile_confirm_delete.html'
    success_url = reverse_lazy('index')  # Replace 'index' with the actual URL name

    def test_func(self):
        # Check if the user is the owner of the profile or has superuser/admin privileges
        return self.request.user.is_superuser or self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        # Delete user when related profile is deleted
        # Add a success message
        messages.success(request, 'Your profile has been deleted successfully.')
        
        # Logout the user
        logout(request)
        return super().delete(request, *args, **kwargs)
        

# Generic class-based view to generate a list of all authors.
class AuthorListView(ListView):
    template_name = "app/authors_list.html"
    model = Author
    context_object_name = 'author_list'
    paginate_by = 10
    

# Generic class-based view to display information about an author and list of created posts . 
class AuthorDetailView(ListView):
    template_name ='app/author_detail.html'
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        target_author=get_object_or_404(Author, pk = pk)
        target_author.save()
        return Post.objects.filter(author=target_author)
    
    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['author_info'] = get_object_or_404(Author, pk = self.kwargs['pk'])
        return context
    
  
# Generic class-based view for a list of all posts.
class PostListView(ListView): 
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "app/index.html"
    context_object_name = 'post_list'
    paginate_by = 10


# Generic class-based detail view for a post.
class PostDetailView(DetailView):   
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm()
        # post.create_tags()
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "app/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
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

        return render(
            request,
            "app/post_detail.html",
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
        post = get_object_or_404(Post,  slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post-detail', args=[slug]))


# Generic class-based view to create new post.
class PostCreateView(LoginRequiredMixin, CreateView):  
    model = Post
    fields = ["title", "content", "featured_image", 'status', 'categories',"tags"]

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse("index")

    def form_valid(self, form):
        obj = form.save(commit=False)
        new_author = self.request.user.profile
        obj.author = Author.objects.get(profile = new_author)
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        
        # Process categories and tags
        categories = form.cleaned_data.get('categories', [])
        tags = form.cleaned_data.get('tags', [])

        obj.categories.set(categories)
        obj.tags.set(tags)

        return HttpResponseRedirect(self.get_success_url())


# Generic class-based view to update post only by the author of the post.       
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content", "featured_image"]
    template_name = 'app/post_form.html'

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
            raise PermissionError("You are not authorized to update this post.")
        return obj


# Generic class-based view to delete post.
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'app/post_delete.html'
    success_url = reverse_lazy('index')

    def get(self, request, slug, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, slug, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, 'The post has been deleted successfully.')
        return super().post(request, *args, **kwargs)
    

# Generic class-based view for author update comment function.
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['body'] 
    template_name = 'app/comment_update.html' 

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Comment Updated Successfully!!")
        return HttpResponseRedirect(reverse('index'))
    

# Generic class-based view for author delete comment function.
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'app/comment_delete.html' 

    def get(self, request, pk, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        context = {'comment': comment}
        if request.method == 'GET':
            return render(request, 'app/comment_delete.html',context)

    def post(self, request, pk, *args, **kwargs):   
        comment = get_object_or_404(Comment, pk=pk)    
        if request.method == 'POST':
            comment.delete()
            messages.success(request, 'The comment has been deleted successfully.')
        return HttpResponseRedirect(reverse('index'))
    

# View function for a contact form.
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'app/contact.html', {'form': form})


# View function for a successfully sent contact form.
def success(request):
    return render(request, 'app/success.html')


# Function to log out the user and redirect to the registration page.
def logout_and_redirect(request):
    logout(request)
    return redirect('register') 


# Login view function.
@login_required
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index') 
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                pass

        return render(request, 'login.html')


# Function that will be called when a 404 error occurs
def custom_404(request, exception):
    """
    Custom 404 error view.
    """
    return render(request, 'app/404.html', {'exception': exception}, status=404)