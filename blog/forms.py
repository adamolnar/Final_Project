from django import forms
from .models import Post, Comment
from django.shortcuts import render, redirect


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',) 

        def __init__(self, *args, **kwargs):
            super(CommentForm, self).__init__(*args, **kwargs)
            # Set the label for the 'body' field to an empty string
            self.fields['body'].widget.attrs.update({'class': 'hide-label'})

        def clean_body(self):
            # Custom validation for the comment body if needed
            body = self.cleaned_data.get('body')
            # Your validation logic here
            return body
        
    def comment_view(request):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                # Process the form data, save to the database, etc.
                form.save()
                return redirect('post-detail')  # Redirect to the same view to display an empty form again
        else:
            form = CommentForm()

        return render(request, 'blog/post_detail.html', {'form': form})


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


