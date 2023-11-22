from django.db import models

from django.contrib.auth.models import User #Blog author or commenter
from cloudinary.models import CloudinaryField
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


STATUS = ((0, "Draft"), (1, "Published"))

# Model representing a blogger.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="all_authors" )
    bio = models.TextField(max_length=400, help_text="Enter your bio details here.", null=True)
   
    class Meta:
        ordering = ["user"]

    def get_absolute_url(self):
        # Returns the url to access a particular blog-author instance.
        return reverse('author_detail', args=[str(self.id)])

    def __str__(self):
        # String for representing the Model object.
        return self.user.username

# Model representing a category.
class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True, null=False)
 
    def __str__(self):
        return self.title


# Model representing a tag.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.name

# Model representing a blog post.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True )
    slug = models.SlugField(max_length=200, unique=True)
    # author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because Blog can only have one author/User, but bloggsers can have multiple blog posts.
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag, related_name='tag')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        # Returns the URL to access a detail record for this post.
        return reverse('post_detail', args=[str(self.id)])
    


# Model representing a comment against a blog post.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comment")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


