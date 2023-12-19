from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField
from PIL import Image
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.template.defaultfilters import slugify


STATUS = ((0, "Draft"), (1, "Published"))


# Model assigning Profile Page to each user.
class Profile(models.Model):
    about_me = models.TextField()
    image = models.ImageField(upload_to='images/', default='placeholder')
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
    
    def post_count(self):
        return Post.objects.filter(author=self.user.profile.user_id).count()

    def comment_count(self):
        return Comment.objects.filter(author=self.user).count()
    
    def shared_count(self):
        return self.users_profile.aggregate(shared_count=models.Count('blog_posts__likes'))['shared_count'] or 0


# Model representing a blogger.
class Author(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="users_profile"
    )
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    # avatar =  CloudinaryField()
   
    class Meta:
        ordering = ["profile"]

    def get_absolute_url(self):
        # Returns the url to access a particular blog-author instance.
        return reverse('author-detail', kwargs={"pk": self.pk})

    def __str__(self):
        # String for representing the Model object.
        return self.profile.user.username


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
    featured_image = models.ImageField(upload_to='images/', default='placeholder')
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
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comment")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# Model to store contact form informations.
class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.email