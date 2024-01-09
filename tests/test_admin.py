from django.contrib.admin.sites import AdminSite
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from author.models import Author, AuthorAccessRequest
from blog.models import Post, Comment
from author.admin import AuthorAdmin, AuthorAccessRequestAdmin
from blog.admin import CommentAdmin


class AuthorAdminTestCase(TestCase):
    """
    Verifies the functionality of the `AuthorAdmin` class in the Django admin
    panel, focusing on the custom action 'make_author' for authorizing authors.
    """

    def setUp(self):
        """
        Sets up necessary objects for the test:
        Creates a test user (`testuser`) and an associated `Author` object
        (`John Doe`) with `is_authorized` set to `False`.
        """
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        self.author = Author.objects.create(
            profile=self.user.profile, first_name='John', last_name='Doe',
            is_authorized=False)

    def test_make_author_action(self):
        """
        Ensures the custom admin action `make_author` updates an `Author`
        object's `is_authorized` field to `True`.
        """
        request = RequestFactory().get('/admin/')
        request.session = {}
        request._messages = []

        admin = AuthorAdmin(Author, None)
        admin.make_author(request, queryset=[self.author])

        self.author.refresh_from_db()
        self.assertTrue(self.author.is_authorized)

    def tearDown(self):
        """
        Cleans up after each test by deleting the test user and author objects.
        """
        self.user.delete()
        self.author.delete()


class AuthorAccessRequestAdminTestCase(TestCase):
    """
    Verifies functionality of the `AuthorAccessRequestAdmin` class in the
    Django admin panel, focusing on the 'make_author' action for author access
    requests.
    """

    def setUp(self):
        """
        Sets up necessary objects for testing:
        Creates a test user (`testuser`) and an `AuthorAccessRequest` object
        with `is_authorized` set to `False`.
        """
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        self.author_access_request = AuthorAccessRequest.objects.create(
            profile=self.user.profile, request_reason='Test reason',
            is_authorized=False)

    def test_make_author_action(self):
        """
        Verifies if the `make_author` admin action authorizes an
        `AuthorAccessRequest`.
        """
        request = RequestFactory().get('/admin/')
        request.session = {}
        request._messages = []

        admin = AuthorAccessRequestAdmin(AuthorAccessRequest, None)
        admin.make_author(request, queryset=[self.author_access_request])

        self.author_access_request.refresh_from_db()
        self.assertTrue(self.author_access_request.is_authorized)

    def tearDown(self):
        """
        Cleans up after each test by deleting the test user and author access
        request object.
        """
        self.user.delete()
        self.author_access_request.delete()


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
