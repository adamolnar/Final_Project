from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Author, AuthorMessage
from .forms import AuthorMessageForm, AuthorAccessRequestForm
from profile.models import Profile
from blog.models import Post
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
    paginate_by = 6
    

# Generic class-based view to display information about an author and list of created posts. 
class AuthorDetailView(DetailView):
    template_name ='author/author_detail.html'
    model = Author
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_info = self.get_object()
        posts = Post.objects.filter(author=author_info)
        context['author_info'] = author_info
        context['posts'] = posts
        return context


# Generic class-based view to store all messages sent by users to authors.
class MessageAuthorView(FormView):
    template_name = 'author/message_author.html'
    form_class = AuthorMessageForm

    def get_author(self):
        author_id = self.kwargs.get('author_id')
        return get_object_or_404(User, id=author_id)

    def form_valid(self, form):
        author = self.get_author()
        message = AuthorMessage(
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


# Generic class-based view to handle author access requests
class RequestAuthorAccessView(LoginRequiredMixin, FormView):
    template_name = 'author/request_author_access.html'
    form_class = AuthorAccessRequestForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Update the form.instance.profile with the user's profile
            form.instance.profile = request.user.profile
            
            # Create an AuthorAccessRequest instance
            request_reason = form.cleaned_data['request_reason']
           
            # Authorize the request
            form.instance.authorize_request()
            
            messages.success(request, 'Your request has been submitted. We will review it soon.')
            return redirect('index')  # Redirect to the desired page after successful submission

        return render(request, self.template_name, {'form': form})
