from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Comment, Author, Category, Tag, Profile, Contact, AuthorMessage
from django_summernote.admin import SummernoteModelAdmin


# Register the Profile model with the admin site
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('user', 'about_me', 'is_active', 'is_staff', 'is_admin', 'post_count', 'comment_count', 'shared_count')
    # Add filters for the list view
    list_filter = ('user__is_active', 'user__is_staff', 'user__is_superuser')

    # Custom methods for display and actions
    def is_active(self, obj):
        return obj.user.is_active

    is_active.boolean = True
    is_active.short_description = 'Active'

    def is_staff(self, obj):
        return obj.user.groups.filter(name='Staff').exists()

    is_staff.boolean = True
    is_staff.short_description = 'Staff'

    def is_admin(self, obj):
        return obj.user.groups.filter(name='Admin').exists()

    is_admin.boolean = True
    is_admin.short_description = 'Admin'


# Register the Author model with the admin site
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('profile', 'first_name', 'last_name')
    # Add search functionality for the list view
    search_fields = ['profile__user__username', 'first_name', 'last_name']


# Register the AuthorMessage model with the admin site
@admin.register(AuthorMessage)
class AuthorMessageAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('author', 'sender_name', 'sender_email', 'timestamp')
    # Add search functionality for the list view
    search_fields = ['author__username', 'sender_name', 'sender_email']


# Register the Category model with the admin site
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Add prepopulated fields for the admin interface
    prepopulated_fields = {'slug': ('title',)}


# Register the Tag model with the admin site
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # Add prepopulated fields for the admin interface
    prepopulated_fields = {'slug': ('name',)}


# Register the Post model with the admin site
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'slug', 'status', 'created_on')
    # Add search functionality for the list view
    search_fields = ['title', 'content', 'author__profile__user__username']
    # Add filters for the list view
    list_filter = ('author', 'status', 'created_on', 'categories', 'tags')
    # Add prepopulated fields for the admin interface
    prepopulated_fields = {'slug': ('title',)}
    # Use Summernote for the content field
    summernote_fields = ('content',)


# Register the Comment model with the admin site
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    # Add filters for the list view
    list_filter = ('approved', 'created_on')
    # Add search functionality for the list view
    search_fields = ('name', 'email', 'body')
    # Add custom action for the admin interface
    actions = ['approve_comments']

    # Custom action method
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

# Register the Contact model with the admin site
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ['email', 'name', 'message']