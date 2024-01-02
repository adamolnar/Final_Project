from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from django.template.defaultfilters import slugify
from author.models import Author
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Model representing a category.
class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True, null=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
 
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
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default="v1699179858/lakyrzjrxgfb05kpyi2r")
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        # Returns the URL to access a detail record for this post.
        return reverse('post-detail', args=[str(self.id)])
    
    def approved_comments(self):
        return self.comments.filter(approved=True)
    
    


# Model representing a comment against a blog post.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="comment")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
