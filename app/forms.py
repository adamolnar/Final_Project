from .models import Comment
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EditProfileForm(forms.Form):
    username = forms.CharField()
    about_me = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)     


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        
        fields = ('title','content','featured_image', 'status', 'categories', 'tags')


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    