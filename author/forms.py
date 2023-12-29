from django import forms
from .models import AuthorAccessRequest

class AuthorMessageForm(forms.Form):
    sender_name = forms.CharField(max_length=255)
    sender_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class AuthorAccessRequestForm(forms.ModelForm):
    # Form to handle author access requests
    class Meta:
        model = AuthorAccessRequest
        fields = ['request_reason']
        widgets = {'request_reason': forms.Textarea(attrs={'rows': 3})}  # Use a textarea for the request reason



