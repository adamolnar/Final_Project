from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from profile.models import Profile

# Model representing a blogger.
class Author(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="users_profile"
    )
    first_name = models.CharField(max_length=100, default="John")
    last_name = models.CharField(max_length=100, default="Doe")
    is_authorized = models.BooleanField(default=False) 
    # avatar =  CloudinaryField()
   
    class Meta:
        ordering = ["profile"]

    def get_absolute_url(self):
        # Returns the url to access a particular blog-author instance.
        return reverse('author-detail', kwargs={"pk": self.pk})

    def __str__(self):
        # String for representing the Model object.
        return self.profile.user.username
    
    def grant_access(self):
        # Method to grant access to the author
        self.is_authorized = True
        self.save()


# Model to store messages sent by users to authors.    
class AuthorMessage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    sender_name = models.CharField(max_length=255)
    sender_email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender_name} to {self.author.username}'


# Model to store author access requests
class AuthorAccessRequest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    request_reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_authorized = models.BooleanField(default=False)

    def __str__(self):
        return f"Request from {self.profile.user.username}"
    
    def authorize_request(self):
        # Method to authorize the request and update the Author model
        author, created = Author.objects.get_or_create(profile=self.profile)
        if created:
            author.grant_access()
        self.is_authorized = True
        self.save()


