from django.contrib import admin
from .models import Post, Comment, Category, Tag
from django_summernote.admin import SummernoteModelAdmin



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
    list_display = ('title', 'author', 'slug', 'status', 'created_on', 'image')
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

