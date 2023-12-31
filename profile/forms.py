from django import forms
from .models import Contact, Profile
from allauth.account.forms import SignupForm , LoginForm
from project.utils import DivErrorList

class CustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
      super(CustomSignUpForm, self).__init__(*args, **kwargs)
      self.error_class = DivErrorList


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
      super(CustomLoginForm, self).__init__(*args, **kwargs)
      self.error_class = DivErrorList


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["about_me", 'image']

class AuthorMessageForm(forms.Form):
    sender_name = forms.CharField(max_length=255)
    sender_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        

    # Widget customization for the field
        # widgets = {
        #     'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter your message here...'}),
        # }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['message'].widget.attrs['placeholder'] ='Enter your message here...'

    def clean_email(self):
        # Custom validation for the email field if needed
        email = self.cleaned_data.get('email')
        # Your validation logic here
        return email
    
    