from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.template import loader
from .models import Post, Author, Profile, Comment, Tag
from django.contrib.auth.models import User #Blog author or commenter
from .forms import CommentForm, PostForm, ContactForm, ExploreForm
from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail
from cloudinary.models import CloudinaryField
from PIL import Image
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin


# Generic class-based view to create user profile with signals.py automatically after login.
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'app/profile.html'
   
    
# Generic class-based view to update loged in user profile.
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["about_me", 'image']

# Generic class-based view for user to deactivate their profile.    
class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    # template_name = 'app/profile_confirm_delete.html'

    # def get_queryset(self):
    #     owner = self.request.user
    #     return self.model.objects.filter(user=owner)

    # def get(self, request, pk):
    #     profile =  Profile.objects.get(user = request.user)
    #     return render(request, self.template_name, {'profile': profile})

    # def post(self, request, pk):
    #     owner = self.request.user
    #     profile = request.user.profile
    #     print(owner, profile)
    #     if owner == profile:
    #         profile.is_active = False
    #         owner.is_active = False
    #         profile.save()
    #         owner.save()
    #         logout(request)
    #     else:
    #         return HttpResponseNotFound("<h1>Profile not found</h1>")
    #     return redirect('index')

    def delete_user(request, self):
        if request.method == 'DELETE':
            try:
                user_pk = request.user.pk
                User.objects.filter(pk=user_pk).update(is_active=False)
                logout(request)
                messages.success(request, 'Your profile has been deleted.')
                return HttpResponseRedirect(self.get_success_url())
            except Exception as e: 
                HttpResponseNotFound("<h1>Something went wrong!</h1>")
        else:
            return HttpResponseNotFound("<h1>Profile not found</h1>")

    def get_success_url(self):
        return reverse('index')



# Generic class-based view to generate list of all authors.
class AuthorListView(ListView):
    template_name = "app/authors_list.html"
    model = Author
    

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
    paginate_by = 5


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
    model =Post
    form_class = PostForm
    

    def form_valid(self, form):
        post = form.save(commit=False)
        new_author = self.request.user.profile
        post.author = Author.objects.get(profile = new_author)
        post.slug = slugify(form.cleaned_data['title'])
        post.save()
        messages.success(self.request, 'Your post has been created successfully.')
        return redirect('post-detail', slug = post.slug)


# Generic class-based view to update post only by the author of the post.       
class PostUpdateView(LoginRequiredMixin, UpdateView):
    pass
    # model =Post
    # fields = ['content']
    # template_name = 'app/post_form.html'
    
    # def post_edit(request, slug):
    #     post = get_object_or_404(Post, slug=slug)
    #     if request.method == "POST":
    #         form = PostForm(request.POST, instance=post)
    #         if form.is_valid():
    #             post = form.save(commit=False)
    #             new_author = request.user.profile
    #             post.author = Author.objects.get(profile = new_author)
    #             post.created_on = timezone.now()
    #             post.save()
    #             messages.success(request, 'Your post has been updated successfully.')
    #             return redirect('post-detail', slug = post.slug)
    #     else:
    #         form = PostForm(instance=post)
    #     return render(request, 'app/post_update.html', {'form': form})


# Generic class-based view to delete post.
class PostDeleteView(LoginRequiredMixin, DeleteView):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        context = {'post': post}
        if request.method == 'GET':
            return render(request, 'app/post_delete.html',context)

    def post(self, request, slug, *args, **kwargs):   
        post = get_object_or_404(Post, slug=slug)    
        if request.method == 'POST':
            post.delete()
            messages.success(request, 'The post has been deleted successfully.')
        return HttpResponseRedirect(reverse('index'))
    

# @login_required
# def post_edit(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             new_author = request.user.profile
#             post.author = Author.objects.get(profile = new_author)
#             post.created_on = timezone.now()
#             post.save()
#             messages.success(request, 'Your post has been updated successfully.')
#             return redirect('post-detail', slug = post.slug)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'app/post_update.html', {'form': form})



class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['body']  # What needs to appear in the page for update
    template_name = 'app/post_detail.html'  # <app>/<model>_<viewtype>.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return reverse('post-detail', kwargs=dict(slug=self.kwargs['slug']))
    

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    pass
    # model = Comment
    # template_name = 'app/comment_delete.html'  # <app>/<model>_<viewtype>.html

    # def form_invalid(self, form):
    #     return HttpResponseRedirect(self.get_success_url())

    # def get_success_url(self):
    #     return reverse('post-detail', kwargs=dict(slug=self.kwargs['slug']))







def contact(request):
    pass

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             pass
#             return redirect('success')
#     else:
#         form = ContactForm()
#     return render(request, 'app/contact.html', {'form': form})


def success(request):
    pass
#     return render(request, 'app/success.html')

# # Generic class-based view to look for a tag and filter the posts by the given name.
class ExploreView(ListView):
    pass

#   def get(self, request, *args, **kwargs):
#     explore_form = ExploreForm()
#     query = self.request.GET.get('query')
#     tag = Tag.objects.filter(name=query).first()

#     if tag:
#         # Filter posts by tag
#         posts = Post.objects.filter(tags__in=[tag])

#     else:
#         # Show all posts
#         posts = Post.objects.all()
#         context = {
#         'tag': tag,
#         'posts': posts,
#         'explore_form': explore_form,
#         }
#     return render(request, 'app/index.html', context)

#     def post(self, request, *args, **kwargs):
#         explore_form = ExploreForm(request.POST)
#         if explore_form.is_valid():
#             query = explore_form.cleaned_data['query']
#             tag = Tag.objects.filter(name=query).first()
#             posts = None
#             if tag:
#                 # filter posts by tag
#                 posts = Post.objects.filter(tags__in=[tag])
#             if posts:
#                 context = {
#                 'tag': tag,
#                 'posts': posts
#                 }
#             else:
#                 context = {
#                 'tag': tag
#                 }
#             return HttpResponseRedirect(f'/templates/app/index?query={query}')
#     return HttpResponseRedirect('/templates/app/index/')