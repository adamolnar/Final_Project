from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from profile.models import Profile  # Assuming you have a 'Profile' model

# Model representing a blogger.
class Author(models.Model):
    # A ForeignKey relationship to the user's profile
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="users_profile"
    )
    
    # First name of the author (with a default value)
    first_name = models.CharField(max_length=100, default="John")
    
    # Last name of the author (with a default value)
    last_name = models.CharField(max_length=100, default="Doe")
    
    # Indicates whether the author is authorized
    is_authorized = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["profile"]

    def get_absolute_url(self):
        # Returns the URL to access a particular blog-author instance.
        return reverse('author-detail', kwargs={"pk": self.pk})

    def __str__(self):
        # String representation of the Model object.
        return self.profile.user.username
    
    def grant_access(self):
        # Method to grant access to the author
        self.is_authorized = True
        self.save()

# Model to store messages sent by users to authors.    
class AuthorMessage(models.Model):
    # ForeignKey relationship to the author
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    
    # Sender's name for the message
    sender_name = models.CharField(max_length=255)
    
    # Sender's email address for the message
    sender_email = models.EmailField()
    
    # The content of the message
    message = models.TextField()
    
    # Timestamp of when the message was created
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation of the message
        return f'Message from {self.sender_name} to {self.author.username}'

# Model to store author access requests
class AuthorAccessRequest(models.Model):
    # ForeignKey relationship to the user's profile (assuming 'Profile' model exists)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    
    # Reason for requesting author access
    request_reason = models.TextField()
    
    # Timestamp of when the request was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Indicates whether the request is authorized
    is_authorized = models.BooleanField(default=False)

    def __str__(self):
        # String representation of the request
        return f"Request from {self.profile.user.username}"
    
    def authorize_request(self):
        # Method to authorize the request and update the Author model
        author, created = Author.objects.get_or_create(profile=self.profile)
        if created:
            author.grant_access()
        self.is_authorized = True
        self.save()
