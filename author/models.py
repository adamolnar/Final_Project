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
    # avatar =  CloudinaryField()
   
    class Meta:
        ordering = ["profile"]

    def get_absolute_url(self):
        # Returns the url to access a particular blog-author instance.
        return reverse('author-detail', kwargs={"pk": self.pk})

    def __str__(self):
        # String for representing the Model object.
        return self.profile.user.username


# Model to store messages sent by users to authors.    
class AuthorMessage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    sender_name = models.CharField(max_length=255)
    sender_email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender_name} to {self.author.username}'


