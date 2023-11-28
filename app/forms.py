from .models import Comment
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from cloudinary.models import CloudinaryField
from PIL import Image

class EditProfileForm(forms.Form):
    username = forms.CharField()
    about_me = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)

    # The username validation method
    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def clean_username(self):
        """
        This function throws an exception if the username has already been 
        taken by another user
        """

        username = self.cleaned_data['username']
        if username != self.original_username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    'A user with that username already exists.')
        return username


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
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    