from django import forms
from .models import Post, Comment, Contact, Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["about_me", 'image']

class AuthorMessageForm(forms.Form):
    sender_name = forms.CharField(max_length=255)
    sender_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',) 

        # Widget customization for the 'body' field
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your comment here...'}),
        }

        def clean_body(self):
            # Custom validation for the comment body if needed
            body = self.cleaned_data.get('body')
            # Your validation logic here
            return body


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','featured_image', 'status', 'categories', 'tags')

        # Widget customization for the 'content' field
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter your post content here...'}),
            # Add more widget customization if needed
        }

        def clean_title(self):
            # Custom validation for the post title if needed
            title = self.cleaned_data.get('title')
            # Your validation logic here
            return title


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    # Widget customization for the 'message' field
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter your message here...'}),
            # Add more widget customization if needed
        }

    def clean_email(self):
        # Custom validation for the email field if needed
        email = self.cleaned_data.get('email')
        # Your validation logic here
        return email
    