from .models import Comment
from django import forms
from .models import Post, Profile
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


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(validators=[EmailValidator()])

# create a search form to filter the explore page by other tags, 
# allowing the user to search for posts with specific tags    
class ExploreForm(forms.Form):
  query = forms.CharField(
  label='',
  widget=forms.TextInput(attrs={
    'placeholder': 'Explore tags'
    })
  )
    