from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Post, Author
from django.contrib.auth.models import User #Blog author or commenter
from .forms import CommentForm, PostForm, EditProfileForm
from django.shortcuts import render
from django.utils import timezone
from django.core.mail import send_mail


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            about_me = form.cleaned_data["about_me"]
            username = form.cleaned_data["username"]
            image = form.cleaned_data["image"]

            user = User.objects.get(id=request.user.id)
            profile = Author.objects.get(user=user)
            user.username = username
            user.save()
            profile.about_me = about_me
            if image:
                profile.image = image
            profile.save()
            return redirect("profile", username=user.username)
    else:
        form = EditProfileForm()
    return render(request, "edit_profile.html", {'form': form})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Author, user=user)
    return render(request, 'profile.html', {'profile': profile, 'user': user})




#  Generic class-based view for a list of authors.
class AuthorList(generic.ListView):
    template_name = "all_authors.html"
    model = Author
    queryset = Author.objects.all()
   

    # def queryset(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the posts
    #     context["all_authors"] = Author.objects.all()
    #     return context


    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(AuthorList, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context['all-authors'] = get_object_or_404(Author, post__author = self.kwargs['user_id'])
    #     return context
        






# Generic class-based detail view for a author 
class AuthorDetail(generic.ListView):
    template_name ='author_detail.html'
   
    # context_object_name = 'author_posts'
    # context_object_name = 'author_detail'

    # def get_queryset(self):
    #     self.post = get_object_or_404(Post, pk=self.kwargs['pk'])
    #     self.author = get_object_or_404(Author, pk=self.kwargs['pk'])
    #     return Post.objects.filter(self.author==self.post)
     
    def get_queryset(self):
        pk = self.kwargs['pk']
        target_author=get_object_or_404(Author, pk = pk)
        target_author.save()
        return Post.objects.filter(author=target_author)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['author_detail'] = get_object_or_404(Author, pk = self.kwargs['pk'])
        return context
    



# ------------------------------------------------------------------------------------------

def post_new(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # Return an object without saving to the DB
            post.author = Author.objects.get(pk=request.user.id) # Add an author field which will contain current user's id
            post.slug = post.title
            post.save() # Save the final "real form" to the DB
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
    

#-------------------------------------------------------------------------------------------   
    

# Generic class-based view for a list of all posts.
class PostList(generic.ListView):
    
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    context_object_name = 'post_list'
    paginate_by = 5

# Generic class-based detail view for a post.
class PostDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
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
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            comment_form = CommentForm()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "approved":True,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )
    
    
# # Generic class-based  view for a like/unlike.
class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post,  slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))






    







# class ContactFormView(View):
#     if form.is_valid(self, :
#         form = ContactForm(request.POST)
#         subject = form.cleaned_data["subject"]
#         message = form.cleaned_data["message"]
#         sender = form.cleaned_data["sender"]
#         cc_myself = form.cleaned_data["cc_myself"]

#         if cc_myself:
#             recipients.append(sender)

#         send_mail(subject, message, sender, recipients)
#         return HttpResponseRedirect("/thanks/")