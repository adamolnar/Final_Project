from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Author, AuthorMessage
from blog.models import Post
from .forms import AuthorMessageForm
from django.views.generic import (
    ListView,
    DetailView,
    FormView
)

# Generic class-based view to generate a list of all authors.
class AuthorListView(ListView):
    template_name = "author/authors_list.html"
    model = Author
    context_object_name = 'author_list'
    paginate_by = 10
    

# Generic class-based view to display information about an author and list of created posts . 
class AuthorDetailView(DetailView):
    template_name ='author/author_detail.html'
    model = Author
    
    def get_queryset(self):
        author_id = self.kwargs['pk']
        return Post.objects.filter(author_id=author_id)
    
    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        author_info = self.get_object()
        context['author_info'] = author_info
        return context

# Generic class-based to store all messages sent by users to authors.
class MessageAuthorView(FormView):
    template_name = 'author/message_author.html'
    form_class = AuthorMessageForm

    def get_author(self):
        author_id = self.kwargs.get('author_id')
        return get_object_or_404(User, id=author_id)

    def form_valid(self, form):
        author = self.get_author()
        message = AuthorMessage(
            author=author,
            sender_name=form.cleaned_data['sender_name'],
            sender_email=form.cleaned_data['sender_email'],
            message=form.cleaned_data['message'],
        )
        message.save()
        messages.success(self.request, 'Your message has been sent successfully!')
        return redirect('author-detail', pk=author.id)  # Redirect to the author's detail page or modify as needed

    def form_invalid(self, form):
        author = self.get_author()
        return self.render_to_response({'form': form, 'author': author})   
  
  