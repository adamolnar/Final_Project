from .models import Comment
from django import forms
from .models import Post, Profile, Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from cloudinary.models import CloudinaryField
from PIL import Image
from django.core.validators import EmailValidator



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)     


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        context_object_name = 'write_new_post'
        
        fields = ('title','content','featured_image', 'status', 'categories', 'tags')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

# create a search form to filter the explore page by other tags, 
# allowing the user to search for posts with specific tags    
class ExploreForm(forms.Form):
  query = forms.CharField(
  label='',
  widget=forms.TextInput(attrs={
    'placeholder': 'Explore tags'
    })
  )
    