from django.contrib import admin
from .models import Profile, Contact


# Register the Profile model with the admin site
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('user', 'about_me', 'is_active', 'is_staff', 'is_admin')

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


# Register the Contact model with the admin site
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ['email', 'name', 'message']
