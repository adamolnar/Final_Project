from django.contrib import admin
from .models import Author, AuthorMessage


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

