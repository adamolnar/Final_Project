from django import forms
from .models import Post, Comment


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
        fields = ('title','content','image', 'status', 'categories', 'tags')

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


