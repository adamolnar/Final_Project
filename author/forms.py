from django import forms
from .models import AuthorAccessRequest

# Form for composing author messages
class AuthorMessageForm(forms.Form):
    # Field for sender's name, limited to 255 characters
    sender_name = forms.CharField(max_length=255)
    
    # Field for sender's email address, validating it as an email
    sender_email = forms.EmailField()
    
    # Field for the message, displayed as a textarea
    message = forms.CharField(widget=forms.Textarea)

# Form for handling author access requests
class AuthorAccessRequestForm(forms.ModelForm):
    class Meta:
        model = AuthorAccessRequest
        
        # Specify the fields from the model to include in the form
        fields = ['request_reason']
        
        # Customize the request_reason field's widget to use a textarea
        widgets = {
            'request_reason': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter your reason for author access...'})
        }

