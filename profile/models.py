from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField



# Model assigning Profile Page to each user.
class Profile(models.Model):
    about_me = models.TextField()
    image = CloudinaryField('image', default="v1704034646/static/images/avatar.b2e01619cc46")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    
    @property
    def is_active(self):
        return self.user.is_active

    @property
    def is_staff(self):
        return self.user.groups.filter(name='Staff').exists()

    @property
    def is_admin(self):
        return self.user_profile.groups.filter(name='Admin').exists()
    
    def favorite_post(self, post):
        self.favorite_posts.add(post)

    def has_favorited_post(self, post):
        return self.favorite_posts.filter(pk=post.pk).exists()
    

# Model to store contact form informations.
class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    name = models.CharField(max_length=50, )

    def __str__(self):
        return self.email

