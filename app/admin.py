from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Comment, Author, Category, Tag, Profile, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'about_me', 'is_active', 'is_staff', 'is_admin')
    list_filter = ('user__is_active', 'user__is_staff', 'user__is_superuser')
   
    def is_active(self, obj):
        return obj.user.is_active
    is_active.boolean = True
    is_active.short_description = 'Active'

    def is_staff(self, obj):
        return obj.user.is_staff
    is_staff.boolean = True
    is_staff.short_description = 'Staff'

    def is_admin(self, obj):
        return obj.user.is_superuser
    is_admin.boolean = True
    is_admin.short_description = 'Admin'

    def save_model(self, request, obj, form, change):
        # Perform custom actions when saving a Profile instance
        # For example, assign user to 'Staff' group if is_staff is True
        if obj.user.is_staff:
            staff_group, created = Group.objects.get_or_create(name='Staff')
            staff_group.user_set.add(obj.user)
        # Similarly, you can handle 'Admin' group based on is_admin value

        obj.save()

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('profile', )

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title','author', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content', 'author']
    list_filter = ('author','status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'message' ]