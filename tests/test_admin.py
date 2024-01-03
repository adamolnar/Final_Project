from django.contrib.admin.sites import AdminSite
from django.contrib.admin.sites import site as default_admin_site 
from django.test import TestCase, RequestFactory
from author.models import Author, AuthorAccessRequest
from blog.models import Post
from django.contrib.auth.models import User 
from author.admin import AuthorAdmin, AuthorAccessRequestAdmin
from blog.admin import CommentAdmin  
from blog.models import Comment 


class AuthorAdminTestCase(TestCase):
    def setUp(self):
        # Create a user and an author object for testing
        self.user = User.objects.create_user(username='testuser', password='password')
        self.author = Author.objects.create(profile=self.user.profile, first_name='John', last_name='Doe', is_authorized=False)

    def test_make_author_action(self):
        # Create a mock request object with session and messages enabled
        request = RequestFactory().get('/admin/')
        request.session = {}
        request._messages = []

        # Call the make_author action on the AuthorAdmin
        AuthorAdmin(Author, None).make_author(request, queryset=[self.author])

        # Reload the author object from the database
        self.author.refresh_from_db()

        # Check if the author is now authorized
        self.assertTrue(self.author.is_authorized)

    def tearDown(self):
        # Clean up by deleting the test user and author
        self.user.delete()
        self.author.delete()

class AuthorAccessRequestAdminTestCase(TestCase):
    def setUp(self):
        # Create a user and an author access request object for testing
        self.user = User.objects.create_user(username='testuser', password='password')
        self.author_access_request = AuthorAccessRequest.objects.create(
            profile=self.user.profile,
            request_reason='Test reason',
            is_authorized=False
        )

    def test_make_author_action(self):
        # Create a mock request object with session and messages enabled
        request = RequestFactory().get('/admin/')
        request.session = {}
        request._messages = []

        # Call the make_author action on the AuthorAccessRequestAdmin
        AuthorAccessRequestAdmin(AuthorAccessRequest, None).make_author(request, queryset=[self.author_access_request])

        # Reload the author access request object from the database
        self.author_access_request.refresh_from_db()

        # Check if the author access request is now authorized
        self.assertTrue(self.author_access_request.is_authorized)

    def tearDown(self):
        # Clean up by deleting the test user and author access request
        self.user.delete()
        self.author_access_request.delete()

class CommentAdminTest(TestCase):
    def setUp(self):
        # Create a Django admin site for testing
        self.admin_site = AdminSite()
         # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')

        # Create a test author associated with the test user
        self.author = Author.objects.create(profile=self.user.profile)

        # Create some test posts for the author
        self.post1 = Post.objects.create(title='Post 1', content='Content 1', author=self.author, status=1)
        self.post2 = Post.objects.create(title='Post 2', content='Content 2', author=self.author, status=1)

    def test_approve_comments_action(self):
        # Create some test comments with 'approved' set to False
        comment1 = Comment.objects.create(
            name='User1',
            body='Comment body 1',
            post=self.post1,
            approved=True,
        )
        comment2 = Comment.objects.create(
            name='User2',
            body='Comment body 2',
            post=self.post2,
            approved=True,
        )

        # Create an instance of the CommentAdmin class for testing
        comment_admin = CommentAdmin(Comment, self.admin_site)

        # Simulate selecting the test comments in the admin interface
        selected_comments = Comment.objects.filter(pk__in=[comment1.pk, comment2.pk])

        # Run the 'approve_comments' custom action
        comment_admin.approve_comments(None, selected_comments)

        # Verify that the comments have been approved
        comment1.refresh_from_db()
        comment2.refresh_from_db()

        self.assertTrue(comment1.approved)
        self.assertTrue(comment2.approved)

    # Add more test cases as needed
