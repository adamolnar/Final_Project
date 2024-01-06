from django import forms
from .models import Contact, Profile
from allauth.account.forms import SignupForm, LoginForm


# CustomSignUpForm extends the SignupForm
class CustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        # Set the error_class to DivErrorList for customized error rendering


# CustomLoginForm extends the LoginForm
class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        # Set the error_class to DivErrorList for customized error rendering


# ProfileUpdateForm for updating user profiles
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["about_me", 'image']


# AuthorMessageForm for sending messages to authors
class AuthorMessageForm(forms.Form):
    sender_name = forms.CharField(max_length=255)
    sender_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


# ContactForm for handling contact information
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # Customize widget attributes (placeholders) for name, email, and message fields
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter your message here...'

    def clean_email(self):
        # Custom validation for the email field if needed
        email = self.cleaned_data.get('email')
        # Your validation logic here
        return email