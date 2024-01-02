from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from blog.models import Post, Comment
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
        return self.user.groups.filter(name='Admin').exists()
    
    # def post_count(self):
    #     return Post.objects.filter(author=self.user.profile.user_id).count()

    # def comment_count(self):
    #     return Comment.objects.filter(author=self.user).count()
    
    def shared_count(self):
        return self.users_profile.aggregate(shared_count=models.Count('blog_posts__likes'))['shared_count'] or 0



# Model to store contact form informations.
class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    name = models.CharField(max_length=50, )

    def __str__(self):
        return self.email

