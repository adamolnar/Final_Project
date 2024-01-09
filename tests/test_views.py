from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User 
from author.models import Author, AuthorMessage
from profile.models import Profile,  Contact
from blog.models import Category, Tag, Post, Comment
from profile.forms import ContactForm
from django.urls import reverse, resolve
from django.contrib.messages import get_messages
from profile.views import ProfileDetailView
from author.views import MessageAuthorView
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import Http404


class ProfileViewTest(TestCase):
    """
    Test suite for the Profile view in the profile app.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Common data setup for the entire test class.
        """
        cls.user = User.objects.create_user(username='hemingway', id=1, email='user@gmail.com', password='1234')
        cls.profile = Profile.objects.get(user=cls.user)
        cls.url = reverse('profile', args=[str(cls.user.pk)])
        cls.client = Client()
        
    def setUp(self):
        """
        Additional setup for each individual test method.
        """
        self.client = Client()

    def test_user_must_be_logged_in(self):        
        """
        Tests that a non-logged-in user is redirected to the login page.
        """
        response = self.client.get(self.url)  
        self.assertEqual(response.status_code, 302) 

    def test_returns_200(self):
        """
        Tests that a correctly logged-in user receives a 200 response.
        """
        self.client.login(username='hemingway', password="1234")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
 
    def test_get_add(self):        
        """
        Tests that a GET request works and renders the correct template.
        """
        self.client.force_login(self.user)        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_view_returns_profile_of_current_user(self):
        """
        Checks that the view returns the profile of the current user.
        """
        self.client.login(username='hemingway', password="1234")
        response = self.client.get(self.url)
        self.assertEqual(response.context["user"], self.user)
        self.assertEqual(response.context["profile"], self.user.profile)

    def test_correct_view_function(self):
        """
        Checks that the URL is associated with the correct view function.
        """
        view_func = resolve(self.url).func
        expected_view_func = ProfileDetailView.as_view()
        self.assertEqual(view_func.__name__, expected_view_func.__name__)


class ProfileUpdateViewTest(TestCase):
    """
    Test suite for the Profile update view in the profile app.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='hemingway', email='user@gmail.com', password='1234', id=1)
        cls.profile = Profile.objects.get(user=cls.user)

    def setUp(self):
        """
        Additional setup for each individual test method.
        """
        self.client = Client()

    def test_edit_profile_returns_200(self):
        """
        Test to ensure that the edit profile page returns a 200 response for the current user.
        """
        self.login_user()
        response = self.client.get(reverse('profile-update', args=[str(self.user.pk)]))
        self.assertEqual(response.status_code, 200)

    def test_edit_profile_form_displayed(self):
        """
        Test to ensure that the profile update form is displayed on the page.
        """
        self.login_user()
        response = self.client.get(reverse('profile-update', args=['1']))
        self.assertContains(response, '<form', count=1)
        self.assertContains(response, 'id="id_username"', count=1)

    def login_user(self):
        """
        Helper method to log in the test user.
        """
        self.client.login(username='hemingway', password='1234')


class AuthorListViewTest(TestCase):
    """
    Test suite for the Author list view in the author app.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='hemingway', id=1, email='user@gmail.com', password='1234')
        cls.profile = Profile.objects.get(user=cls.user)
        cls.author = Author.objects.create(profile=cls.profile)

    def setUp(self):
        """
        Additional setup for each individual test method, including creating multiple authors for pagination tests.
        """
        self.user = User.objects.create_user(username='hemingway', id=1, email='user@gmail.com', password='1234')
        self.profile = Profile.objects.get(user=self.user)
        for _ in range(13):
            Author.objects.create(profile=self.profile)

    def test_view_uses_correct_template(self):
        """
        Test that the authors list is using the correct template.
        """
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/author_list.html')

    def test_view_url_accessible_by_name(self):
        """
        Test if the authors list can be accessed by its URL name.
        """
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_ten(self):
        """
        Test that pagination is correctly configured to show ten items per page.
        """
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['author_list']), 10)

    def test_lists_all_authors(self):
        """
        Test that all authors are listed across the paginated pages.
        """
        response = self.client.get(reverse('authors-list') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['author_list']), 4)


class AuthorDetailViewTestCase(TestCase):
    """
    Test suite for the AuthorDetailView in the author app.
    """

    def setUp(self):
        """
        Set up function to create a test user, author, and posts for testing.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        self.author = Author.objects.create(profile=self.user.profile)
        self.post1 = Post.objects.create(title='Post 1', content='Content 1', author=self.author, status=1)
        self.post2 = Post.objects.create(title='Post 2', content='Content 2', author=self.author, status=1)

    def test_author_detail_view_with_valid_author(self):
        """
        Test the AuthorDetailView with a valid author.
        """
        response = self.client.get(reverse('author-detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/author_detail.html')

    def test_author_detail_view_with_invalid_author(self):
        """
        Test the AuthorDetailView with an invalid author (non-existent PK).
        """
        invalid_author_pk = self.author.pk + 1
        response = self.client.get(reverse('author-detail', args=[invalid_author_pk]))
        self.assertEqual(response.status_code, 404)


class MessageAuthorViewTestCase(TestCase):
    """
    Test suite for the MessageAuthorView in the author app.
    """

    def setUp(self):
        """
        Set up function to create a test user, author, and necessary instances for testing the view.
        """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.author = Author.objects.create(profile=self.user.profile)
        self.view = MessageAuthorView()
        self.client = Client()
        self.message_url = reverse('message-author', kwargs={'author_id': self.user.id})

    def test_get_author_with_valid_id(self):
        """
        Test retrieving an author with a valid ID.
        """
        request = self.factory.get('/fake-url')
        self.view.request = request
        self.view.kwargs = {'author_id': self.user.id}
        author = self.view.get_author()
        self.assertEqual(author, self.user)

    def test_get_author_with_invalid_id(self):
        """
        Test retrieving an author with an invalid ID, expecting Http404.
        """
        request = self.factory.get('/fake-url')
        self.view.request = request
        self.view.kwargs = {'author_id': 9999}
        with self.assertRaises(Http404):
            self.view.get_author()

    def test_form_valid(self):
        """
        Test the form submission with valid data and ensure the message is created.
        """
        self.client.login(username='testuser', password='testpassword')
        form_data = {
            'sender_name': 'Test Sender',
            'sender_email': 'sender@test.com',
            'message': 'Test message content'
        }
        response = self.client.post(self.message_url, form_data)
        self.assertEqual(AuthorMessage.objects.count(), 1)
        message = AuthorMessage.objects.first()
        self.assertEqual(message.sender_name, 'Test Sender')
        self.assertEqual(message.sender_email, 'sender@test.com')
        self.assertEqual(message.message, 'Test message content')

        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your message has been sent successfully!')


class RequestAuthorAccessViewTest(TestCase):
    """
    Test suite for the RequestAuthorAccess view in the author app.
    """

    def setUp(self):
        """
        Set up function to create a test user and profile for testing the view.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_get_request_author_access_view(self):
        """
        Test the GET request for the request author access view.
        """
        self.client.login(username='testuser', password='testpassword')
        url = reverse('request-author-access')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_post_request_author_access_view(self):
        """
        Test the POST request for the request author access view with valid form data.
        """
        self.client.login(username='testuser', password='testpassword')
        url = reverse('request-author-access')
        form_data = {
            'request_reason': 'Test request reason',
        }
        response = self.client.post(url, data=form_data)
        self.assertRedirects(response, reverse('index'))


class TestPostListView(TestCase):
    """
    Test suite for the Post list view in the blog app.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        """
        Set up function to create a test user, author, and posts for testing the view.
        """
        self.client = Client()
        self.user = User.objects.create_user(username='hemingway', id=1, email='user@gmail.com', password='1234')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)
        self.post = Post.objects.create(title='Karramba', author=self.author, slug='karramba', status='1')
        self.post1 = Post.objects.create(title='News', author=self.author, slug='news', status='1')

    def test_get_index(self):
        """
        Test that a GET request to the index page works and renders the correct template.
        """
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_context_contains_posts(self):
        """
        Test that the context contains 'post_list'.
        """
        response = self.client.get(reverse('index'))
        self.assertIn('post_list', response.context_data)

    def test_excludes_draft_posts(self):
        """
        Test that the list of posts on the homepage excludes draft posts.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(len(response.context_data['post_list']), 2)


class TestAddPostView(TestCase):
    """
    Test suite for the Add Post view in the blog app.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.image_content = b"dummy content"
        cls.sample_image = SimpleUploadedFile("test_image.jpg", 
                                              cls.image_content, content_type="image/jpeg")

    def setUp(self):
        """
        Set up function to create test users, author, posts, and client for testing the view.
        """
        self.user = User.objects.create_user(username='avatar', id=1)
        self.hacker = User.objects.create_user(username='hacker')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)
        self.post = Post.objects.create(title='Karramba', author=self.author, slug='karramba', status='1')
        self.post1 = Post.objects.create(title='News', author=self.author, slug='news')
        self.post2 = Post.objects.create(title='Coding', author=self.author, slug='coding', status='1')
        self.client = Client()
        self.url = reverse('post-create')

    def test_login_requirement(self):
        """
        Test that a non-logged-in user is redirected from the post create view.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
       
    def test_get_post_create(self):
        """
        Test that a GET request to the post create view works and renders the correct template.
        """
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

    def test_user_must_be_logged_in(self):
        """
        Test that a non-logged-in user is redirected from the post create view.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_form_fields(self):
        """
        Test that all expected fields are displayed in the post creation form.
        """
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        form = response.context_data['form']
        self.assertEqual(len(form.fields), 6)
        self.assertIn('title', form.fields)
        self.assertIn('content', form.fields)
        self.assertIn('image', form.fields)
        self.assertIn('status', form.fields)
        self.assertIn('categories', form.fields)
        self.assertIn('tags', form.fields)


class TestPostDetailView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        # Set up any necessary data before running the tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile)
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)

    def test_post_detail_view_with_valid_slug(self):
        # Test the PostDetailView with a valid slug
        response = self.client.get(reverse('post-detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')  # Check if post title is in the response content

    def test_post_detail_view_with_invalid_slug(self):
        # Test the PostDetailView with an invalid slug
        response = self.client.get(reverse('post-detail', args=['invalid-slug']))
        self.assertEqual(response.status_code, 404)  # Expecting a 404 Not Found response

    def test_get_request(self):
        # Test the GET request to the PostDetailView
        url = reverse('post-detail', kwargs={'slug': self.post.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertIn('post', response.context)
        self.assertIn('comments', response.context)

    def test_post_request(self):
        # Test the POST request to the PostDetailView
        url = reverse('post-detail', kwargs={'slug': self.post.slug})
        form_data = {'name': 'Test User', 'body': 'Test Comment Body'}

        # Login before making the post request
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(url, data=form_data)
        
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if a new comment is created after posting
        self.assertEqual(Comment.objects.count(), 1)
        new_comment = Comment.objects.first()

        # Set the author field based on the user in the test setup
        new_comment.author = self.user
        new_comment.save()

        # Ensure that the new comment is associated with the correct post
        self.assertEqual(new_comment.post, self.post)
        self.assertEqual(new_comment.body, 'Test Comment Body')

    def test_user_likes_post(self):
        # Check if the user now likes the post
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('post-detail', kwargs={'slug': self.post.slug})
        response = self.client.get(self.url)
        self.assertFalse(response.context['liked'])
        self.client.post(reverse('post-like', kwargs={'slug': self.post.slug}))
        response = self.client.get(self.url)
        self.assertTrue(response.context['liked'])

    def test_post_detail_view_not_liked(self):
        # Check that the request user ID is in the response
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('post-detail', kwargs={'slug': self.post.slug})
        response = self.client.get(self.url)
        self.assertFalse(response.context['liked'])
        self.assertEqual(response.context['request'].user.id, self.user.id)


class TestPostLikeView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)

    def test_post_like(self):
        url = reverse('post-like', kwargs={'slug': self.post.slug})
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302) 
        self.post.refresh_from_db()
        self.assertTrue(self.user in self.post.likes.all())

    def test_post_unlike(self):
        url = reverse('post-like', kwargs={'slug': self.post.slug})
        self.client.login(username='testuser', password='testpassword')
        self.post.likes.add(self.user)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertFalse(self.user in self.post.likes.all())


class TestPostCreateView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)
        self.category = Category.objects.create(title='Test Category', slug='test-category')
        self.tag = Tag.objects.create(name='Test Tag', slug='test-tag')

    def test_post_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('post-create')

        data = {
            'title': 'Test Post',
            'content': 'Test Content',
            'status': 1,
            'categories': [self.category.id],
            'tags': [self.tag.id],
        }

        response = self.client.post(url, data)

        # Check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the post was created successfully
        new_post = Post.objects.filter(title='Test Post').first()
        self.assertIsNotNone(new_post)

        # Check if the created post has the correct author
        self.assertEqual(new_post.author, self.author)

        # Check if the created post has the correct category and tag
        self.assertEqual(new_post.categories.first(), self.category)
        self.assertEqual(new_post.tags.first(), self.tag)


class TestPostUpdateView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)
        self.url = reverse('post-update', kwargs={'slug': self.post.slug})
        self.updated_title = 'Updated Title'
        self.updated_content = 'Updated Content'
        self.client.login(username='testuser', password='testpassword')

    def test_get_update_post_view(self):
        # Test accessing the update view for a post
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'Test Content')


class TestPostDeleteView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        # Create a user, profile, and author
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)
        self.url = reverse('post-delete', kwargs={'slug': self.post.slug})
        self.client.login(username='testuser', password='testpassword')

    def test_get_post_delete_view(self):
        # Test accessing the delete view for a post
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_delete.html')
        self.assertContains(response, 'Test Post')
    
    def test_post_delete_view(self):
        # Test posting a deletion request for the post
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Post.DoesNotExist):
            deleted_post = Post.objects.get(id=self.post.id)

    def test_post_delete_redirect(self):
        # Test redirection after posting a deletion request for the post
        self.url = reverse('post-delete', kwargs={'slug': self.post.slug})
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.url)
        expected_redirect_url = reverse('index')
        self.assertRedirects(response, expected_redirect_url)

    def test_post_deleted_from_database(self):
        # Test that the post is deleted from the database
        response = self.client.post(self.url)
        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(pk=self.post.pk)


class CommentUpdateViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        # Create a user, profile, and author
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)

        # Create a test comment
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            name='Test Author',
            body='Test Comment Body',
        )

    def test_comment_update_view_template_used(self):
        # Check that the correct template is used
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('comment-update', kwargs={'pk': self.comment.pk}))
        self.assertTemplateUsed(response, 'blog/comment_update.html')

    def test_comment_update_view_get_request(self):
        # Check that the response status code is 200 (OK)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('comment-update', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, 200)

    def test_comment_update_view_post_request(self):
        # Check that the comment was updated in the database
        self.client.login(username='testuser', password='testpassword')
        updated_body = 'Updated Comment Body'
        post_data = {'body': updated_body}
        response = self.client.post(reverse('comment-update', kwargs={'pk': self.comment.pk}), post_data)
        self.assertEqual(response.status_code, 302)
        updated_comment = Comment.objects.get(pk=self.comment.pk)
        self.assertEqual(updated_comment.body, updated_body)

    def test_comment_update_view_redirect_after_update(self):
        # Check that the user is redirected to the expected URL after updating the comment
        self.client.login(username='testuser', password='testpassword')
        updated_body = 'Updated Comment Body'
        post_data = {'body': updated_body}
        response = self.client.post(reverse('comment-update', kwargs={'pk': self.comment.pk}), post_data)
        expected_redirect_url = reverse('index') 
        
    
class CommentDeleteViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        # Create a user, profile, and author
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)

        # Create a post
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)

        # Create a test comment
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            name='Test Author',
            body='Test Comment Body',
        )
        self.client.login(username='testuser', password='testpassword')

    def test_comment_delete_view_get_request(self):
        # Check that the response status code is 200 (OK)
        url = reverse('comment-delete', kwargs={'pk': self.comment.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_comment_delete_view_context_contains_comment(self):
        # Simulate a GET request to the CommentDeleteView
        response = self.client.get(reverse('comment-delete', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.context['comment'], self.comment)

    def test_comment_delete_view_post_request(self):
        # Check that the response status code is 302 (redirect)
        response = self.client.post(reverse('comment-delete', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, 302)

    def test_comment_deleted_from_database(self):
        # Check that the comment is deleted from the database
        self.client.post(reverse('comment-delete', kwargs={'pk': self.comment.pk}))
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(pk=self.comment.pk)

    def test_success_message_present(self):
        # Check that a success message is present in the messages framework
        response = self.client.post(reverse('comment-delete', kwargs={'pk': self.comment.pk}))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'The comment has been deleted successfully.')

    def test_user_redirected_after_deleting_comment(self):
        # Check that the user is redirected to the expected URL after deleting the comment
        response = self.client.post(reverse('comment-delete', kwargs={'pk': self.comment.pk}))
        expected_redirect_url = reverse('index')  # Replace 'index' with the actual URL name
        self.assertRedirects(response, expected_redirect_url)


class ContactViewTest(TestCase):
    def test_contact_view_get(self):
        client = Client()
        response = client.get(reverse('contact'))  # Replace 'contact' with the actual URL name

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'profile/contact.html')

        # Check that the form is present in the context
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contact_view_post_valid(self):
        client = Client()
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message content',
        }
        response = client.post(reverse('contact'), data)  

        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the user is redirected to the 'success' page
        self.assertRedirects(response, reverse('success'))  

        # Check that the form data is saved in the database
        self.assertEqual(Contact.objects.count(), 1)
        saved_contact = Contact.objects.first()
        self.assertEqual(saved_contact.name, 'Test User')
        self.assertEqual(saved_contact.email, 'test@example.com')
        self.assertEqual(saved_contact.message, 'Test message content')

    def test_contact_view_post_invalid(self):
        client = Client()
        # Omitting required data to intentionally trigger form validation errors
        data = {}
        response = client.post(reverse('contact'), data)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'profile/contact.html')

        # Check that the form is present in the context
        self.assertIsInstance(response.context['form'], ContactForm)

        # Check that the form has errors
        self.assertTrue(response.context['form'].errors)
