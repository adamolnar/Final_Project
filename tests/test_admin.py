from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from django.contrib.auth.models import User
from author.models import Author
from blog.models import Post, Comment
from blog.admin import CommentAdmin


class CommentAdminTest(TestCase):
    """
    Checks the functionality of the `CommentAdmin` class within the Django
    admin interface, focusing on custom actions related to comment moderation.
    """

    def setUp(self):
        """
        Sets up objects for testing:
        Creates a Django admin site instance and a test user, author, and posts
        for comments.
        """
        self.admin_site = AdminSite()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword',
                                             email='test@example.com')
        self.author = Author.objects.create(profile=self.user.profile)
        self.post1 = Post.objects.create(title='Post 1', content='Content 1',
                                         author=self.author, status=1)
        self.post2 = Post.objects.create(title='Post 2', content='Content 2',
                                         author=self.author, status=1)

    def test_approve_comments_action(self):
        """
        Verifies if the 'approve_comments' action correctly approves selected
        comments.
        """
        comment1 = Comment.objects.create(name='User1', body='Comment body 1',
                                          post=self.post1, approved=False)
        comment2 = Comment.objects.create(name='User2', body='Comment body 2',
                                          post=self.post2, approved=False)

        comment_admin = CommentAdmin(Comment, self.admin_site)
        selected_comments = Comment.objects.filter(
            pk__in=[comment1.pk, comment2.pk])

        comment_admin.approve_comments(None, selected_comments)

        comment1.refresh_from_db()
        comment2.refresh_from_db()

        self.assertTrue(comment1.approved)
        self.assertTrue(comment2.approved)
