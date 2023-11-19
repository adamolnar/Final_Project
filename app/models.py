from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


STATUS = ((0, "Draft"), (1, "Published"))

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True)
 
    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = CloudinaryField('image', default='placeholder')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
    # Returns the URL to access a particular instance of the model.
        return reverse('profile-detail', args=[str(self.id)])


class Author(models.Model):
    # Model representing an author.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        # Returns the URL to access a particular author instance.
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        # String for representing the Model object.
        return f'{self.last_name}, {self.first_name}'