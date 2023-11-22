from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Post, Author
from django.contrib.auth.models import User #Blog author or commenter
from .forms import CommentForm
from django.shortcuts import render


#  Generic class-based view for a list of authors.
class AuthorList(generic.ListView):
    model = Author
    template_name = "all_authors.html"
    queryset = Author.objects.all()

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

    

    
    

# Generic class-based view for a list of all posts.
class PostList(generic.ListView):
   
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 5

# Generic class-based detail view for a post.
class PostDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
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
        post = get_object_or_404(queryset, slug=slug)
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
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


# # Generic class-based  view for a like/unlike.
class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))



        
   
   

    

