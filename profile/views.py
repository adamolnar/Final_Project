from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Profile
from author.models import Author
from blog.models import Post
from .forms import ContactForm, ProfileUpdateForm
from django.views.generic import (
    DetailView,
    UpdateView,
    DeleteView,
    )


# Generic class-based view to display user profile details.
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile/profile.html'


    def get_object(self, queryset=None):
        return get_object_or_404(Profile, pk=self.kwargs['pk'])
    
    
# Generic class-based view to update logged-in user profile.
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile/profile_form.html'
   

    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated successfully.')
        return super().form_valid(form)
    
    def profile_update_view(request, self):
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Redirect to success page or any other desired page
                
                return redirect('profile')
        else:
            form = ProfileUpdateForm()

        return render(request, 'profile/profile_form.html', {'form': form})


# Generic class-based view to delete user profile. 
class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'profile/profile_confirm_delete.html'
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
        


# View function for a contact form.
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was sent successfully!')
            return redirect('success')
        else:
            messages.error(request, 'Please correct the errors below.')
            
    else:
        form = ContactForm()
    return render(request, 'profile/contact.html', {'form': form})


# View function for a successfully sent contact form.
def success(request):
    return render(request, 'profile/success.html')


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
    return render(request, 'blog/404.html', {'exception': exception}, status=404)