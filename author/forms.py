from django import forms

class AuthorMessageForm(forms.Form):
    sender_name = forms.CharField(max_length=255)
    sender_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


