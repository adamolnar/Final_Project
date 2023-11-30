from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Post, Author, Profile, Comment, Tag
from django.contrib.auth.models import User #Blog author or commenter
from .forms import CommentForm, PostForm, EditProfileForm, ContactForm, ExploreForm
from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail
from cloudinary.models import CloudinaryField
from PIL import Image
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.user.username, request.POST, request.FILES)
        if form.is_valid():
            about_me = form.cleaned_data["about_me"]
            username = form.cleaned_data["username"]
            image = form.cleaned_data["image"]
           
            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            user.save()
            profile.about_me = about_me
            if image:
                profile.image = image
            profile.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect("profile", username=user.username)
    else:
        form = EditProfileForm(request.user.username)
    return render(request, "app/profile_update.html", {'form': form})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'app/profile.html', {'profile': profile, 'user': user})


#  Generic class-based view for a list of authors.
class AuthorListView(ListView):
    template_name = "app/authors_list.html"
    model = Author
    queryset = Author.objects.all()


# Generic class-based detail view for a author 
class AuthorDetailView(DetailView):
    template_name ='app/author_detail.html'
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        target_author=get_object_or_404(Author, pk = pk)
        target_author.save()
        return Post.objects.filter(author=target_author)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['author-detail'] = get_object_or_404(Author, pk = self.kwargs['pk'])
        return context
    

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # Return an object without saving to the DB
            # post = Post.objects.get(post.intsance.pk)
            new_author = Author.objects.get(profile = request.user.id)
            post.author = new_author# Add an author field which will contain current user's id
            post.slug = slugify(post.title)
            post.create_tags()
            post.save() # Save the final "real form" to the DB
            messages.success(request, 'Your post has been created successfully.')
            return redirect('post-detail', slug = post.slug)
    else:
        form = PostForm()
    return render(request, 'app/post_update.html', {'form': form})


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            new_author = request.user.profile
            post.author = Author.objects.get(profile = new_author)
            post.created_on = timezone.now()
            post.save()
            messages.success(request, 'Your post has been updated successfully.')
            return redirect('post-detail', slug = post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'app/post_update.html', {'form': form})

  
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
        post.create_tags()
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
            new_comment.instance.name = request.user.username
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
    
    


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['body']  # What needs to appear in the page for update
    template_name = 'app/post_detail.html'  # <app>/<model>_<viewtype>.html

    def form_valid(self, form):
        form.instance.name = self.request.user.user
        return reverse('post-detail', kwargs=dict(slug=self.kwargs['slug']))
    

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = '#'  # <app>/<model>_<viewtype>.html

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('post-detail', kwargs=dict(slug=self.kwargs['slug']))

# Generic class-based view for a like/unlike.
class PostLikeView(DetailView):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post,  slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post-detail', args=[slug]))


# Generic class-based view to display post detail.
class PostDeleteView(View):

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


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'app/contact.html', {'form': form})


def success(request):
    return render(request, 'app/success.html')

# Generic class-based view to look for a tag and filter the posts by the given name.
class ExploreView(ListView):

  def get(self, request, *args, **kwargs):
    explore_form = ExploreForm()
    query = self.request.GET.get('query')
    tag = Tag.objects.filter(name=query).first()

    if tag:
        # Filter posts by tag
        posts = Post.objects.filter(tags__in=[tag])

    else:
        # Show all posts
        posts = Post.objects.all()
        context = {
        'tag': tag,
        'posts': posts,
        'explore_form': explore_form,
        }
    return render(request, 'app/index.html', context)

    def post(self, request, *args, **kwargs):
        explore_form = ExploreForm(request.POST)
        if explore_form.is_valid():
            query = explore_form.cleaned_data['query']
            tag = Tag.objects.filter(name=query).first()
            posts = None
            if tag:
                # filter posts by tag
                posts = Post.objects.filter(tags__in=[tag])
            if posts:
                context = {
                'tag': tag,
                'posts': posts
                }
            else:
                context = {
                'tag': tag
                }
            return HttpResponseRedirect(f'/templates/app/index?query={query}')
    return HttpResponseRedirect('/templates/app/index/')