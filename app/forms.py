from django import forms
from .models import Post, Comment, Contact, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',) 


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','featured_image', 'status', 'categories', 'tags')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


    