from django.contrib import admin
from .models import Author, AuthorMessage, AuthorAccessRequest


# Register the Author model with the admin site
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('profile', 'first_name', 'last_name', 'is_authorized')
    # Add search functionality for the list view
    search_fields = ['profile__user__username', 'first_name', 'last_name']

    # Define a custom admin action
    actions = ['make_author']

    def make_author(self, request, queryset):
        # Perform the action on selected authors
        for author in queryset:
            author.is_authorized = True
            author.save()

        # Provide a success message to the user
        self.message_user(
            request, 'Successfully marked selected authors as authorized.')

    make_author.short_description = "Mark selected authors as authorized"


# Register the AuthorMessage model with the admin site
@admin.register(AuthorMessage)
class AuthorMessageAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('sender_name', 'sender_email', 'timestamp')
    # Add search functionality for the list view
    search_fields = ['author__username', 'sender_name', 'sender_email']


# Register the AuthorAccessRequest model with the admin site
@admin.register(AuthorAccessRequest)
class AuthorAccessRequestAdmin(admin.ModelAdmin):
    # Admin configuration for the AuthorAccessRequest model
    list_display = ('profile', 'request_reason', 'created_at', 'is_authorized')
    search_fields = ['profile__username', 'profile__email', 'request_reason']

    # Define a custom admin action
    actions = ['make_author']

    def make_author(self, request, queryset):
        # Perform the action on selected authors
        for author in queryset:
            author.is_authorized = True
            author.save()

        # Provide a success message to the user
        self.message_user(
            request, 'Successfully marked selected authors as authorized.')

    make_author.short_description = "Mark selected authors as authorized"
