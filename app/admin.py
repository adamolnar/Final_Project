from django.contrib import admin
from .models import Post, Comment, Author, Category, Tag
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('user', )

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