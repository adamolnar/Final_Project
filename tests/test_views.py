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
    @classmethod
    def setUpTestData(cls):
        # Common data setup for the entire test class
        cls.user = User.objects.create_user(username='hemingway', id=1, email='user@gmail.com', password='1234')
        cls.profile = Profile.objects.get(user=cls.user)
        cls.url = reverse('profile', args=[str(cls.user.pk)])
        cls.client = Client()
        
    def setUp(self):
        # Additional setup for each individual test method
        self.client = Client()

    def test_user_must_be_logged_in(self):        
        # Tests that a non-logged in user is redirected to login page
        response = self.client.get(self.url)  
        self.assertEqual(response.status_code, 302) 

    def test_returns_200(self):
        # Tests correctly logged in user response
        self.client.login(username='hemingway', password="1234")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
 
    def test_get_add(self):        
        # Tests that a GET request works and renders the correct template       
        self.client.force_login(self.user)        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_view_returns_profile_of_current_user(self):
        # Check the profile of the current user
        self.client.login(username='hemingway', password="1234")
        response = self.client.get(self.url)
        self.assertEqual(response.context["user"], self.user)
        self.assertEqual(response.context["profile"], self.user.profile)

    def test_correct_view_function(self):
        # Check that the URL is associated with the correct view function
        view_func = resolve(self.url).func
        expected_view_func = ProfileDetailView.as_view()
        
        # Compare the view functions by their paths or names
        self.assertEqual(view_func.__name__, expected_view_func.__name__)



class ProfileUpdateViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Common setup code that is the same for all test methods

    def setUp(self):
        self.user = User.objects.create_user(username='hemingway', email='user@gmail.com', password='1234', id=1)
        self.profile = Profile.objects.get(user=self.user)

    def test_edit_profile_returns_200(self):
        # Check the profile update belongs to current user
        self.login_user()
        response = self.client.get(reverse('profile-update', args=[str(self.user.pk)]))
        self.assertEqual(response.status_code, 200)

    def test_edit_profile_form_displayed(self):
        # Check that the profile update form is displayed on the page
        self.login_user()
        response = self.client.get(reverse('profile-update', args=['1']))
        self.assertContains(response, '<form', count=1)
        self.assertContains(response, 'id="id_username"', count=1)

    def login_user(self):
        self.client.login(username='hemingway', password='1234')


class AuthorListViewTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='hemingway',id=1, email='user@gmail.com', password='1234')
        cls.profile = Profile.objects.get(user=cls.user) 
        cls.author = Author.objects.create(profile=cls.profile)

    def setUp(self):
        self.user = User.objects.create_user(username='hemingway', id=1, email='user@gmail.com',password='1234')
        self.profile = Profile.objects.get(user=self.user) 
        # Create 13 authors for pagination tests
        number_of_authors = 13

        for profile in range(number_of_authors):
            Author.objects.create(
                profile=self.profile,
            )

    def test_view_uses_correct_template(self):
        # Test that authors list is using correct template
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/author_list.html')

    def test_view_url_accessible_by_name(self):
        # Test if authors list can be accesses by authors name
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_ten(self):
        # Get first page and confirm it has (exactly) remaining 10 items
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['author_list']), 10)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 4 items
        response = self.client.get(reverse('authors-list')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['author_list']), 4)


class AuthorDetailViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')

        # Create a test author associated with the test user
        self.author = Author.objects.create(profile=self.user.profile)

        # Create some test posts for the author
        self.post1 = Post.objects.create(title='Post 1', content='Content 1', author=self.author, status=1)
        self.post2 = Post.objects.create(title='Post 2', content='Content 2', author=self.author, status=1)

    def test_author_detail_view_with_valid_author(self):
        # Test the AuthorDetailView with a valid author
        response = self.client.get(reverse('author-detail', args=[self.author.pk]))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'author/author_detail.html')

    def test_author_detail_view_with_invalid_author(self):
        # Test the AuthorDetailView with an invalid author (non-existent PK)
        invalid_author_pk = self.author.pk + 1
        response = self.client.get(reverse('author-detail', args=[invalid_author_pk]))

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)


class MessageAuthorViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        # Create an author instance associated with the test user
        self.author = Author.objects.create(profile=self.user.profile)
        self.view = MessageAuthorView()
        self.client = Client()
        
        # URL for posting the message
        self.message_url = reverse('message-author', kwargs={'author_id': self.user.id})

    def test_get_author_with_valid_id(self):
        # Mock the request and kwargs for the view
        request = self.factory.get('/fake-url')
        self.view.request = request
        self.view.kwargs = {'author_id': self.user.id}

        # Call the method
        author = self.view.get_author()

        # Assert the retrieved author is correct
        self.assertEqual(author, self.user)

    def test_get_author_with_invalid_id(self):
        # Mock the request and kwargs for the view
        request = self.factory.get('/fake-url')
        self.view.request = request
        self.view.kwargs = {'author_id': 9999}  # Assuming this ID does not exist

        # Assert that Http404 is raised
        with self.assertRaises(Http404):
            self.view.get_author()

    def test_form_valid(self):
        # Log in the user
        self.client.login(username='testauthor', password='testpassword')

        # Prepare form data
        form_data = {
            'sender_name': 'Test Sender',
            'sender_email': 'sender@test.com',
            'message': 'Test message content'
        }

        # Make a POST request with form data
        response = self.client.post(self.message_url, form_data)

        # Check if an AuthorMessage instance has been created
        self.assertEqual(AuthorMessage.objects.count(), 1)
        message = AuthorMessage.objects.first()
        self.assertEqual(message.sender_name, 'Test Sender')
        self.assertEqual(message.sender_email, 'sender@test.com')
        self.assertEqual(message.message, 'Test message content')

        # Check for success message
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your message has been sent successfully!')

class RequestAuthorAccessViewTest(TestCase):
    def setUp(self):
        # Create a test user and profile
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.get(
            user=self.user,
            # Add other required fields for your Profile model
        )

    def test_get_request_author_access_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Get the URL for the request author access view
        url = reverse('request-author-access')  # Replace with the actual URL name

        # Make a GET request to the view
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the 'form' context variable is present in the response
        self.assertIn('form', response.context)

    def test_post_request_author_access_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Get the URL for the request author access view
        url = reverse('request-author-access')  # Replace with the actual URL name

        # Create valid form data
        form_data = {
            'request_reason': 'Test request reason',  # Replace with valid data
            # Add other form fields and their values as needed
        }

        # Make a POST request to the view with valid form data
        response = self.client.post(url, data=form_data)

        # Check that the response redirects to the 'index' page upon successful submission
        self.assertRedirects(response, reverse('index'))  # Replace with the actual URL name


class TestPostListView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='hemingway', id=1, email='user@gmail.com',password='1234')
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile) 
        self.post= Post.objects.create(title='Karramba', author = self.author, slug='karramba',status='1')
        self.post1= Post.objects.create(title='News', author = self.author, slug='news',status='1')
   
    def test_get_index(self):
        # Tests that a get request to index works and renders the correct template
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_context_contains_posts(self):
        #Tests that there the context contains 'post_list' 
        response = self.client.get(reverse('index'))
        self.assertIn('post_list',response.context_data)

    def test_excludes_draft_posts(self):
        # Tests that the list of posts on the homepage excludes drafts
        response = self.client.get(reverse('index'))
        self.assertEqual(len(response.context_data['post_list']), 2)


class TestAddPostView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Create a sample image file for testing
        cls.image_content = b"dummy content"
        cls.sample_image = SimpleUploadedFile("test_image.jpg", 
            cls.image_content, content_type="image/jpeg")

    def setUp(self):
        self.user = User.objects.create_user(username='avatar', id=1)
        self.hacker = User.objects.create_user(username='hacker')
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile)
        self.post= Post.objects.create(title='Karramba', author = self.author, slug='karramba',status='1',)
        self.post1= Post.objects.create(title='News', author = self.author, slug='news')
        self.post2= Post.objects.create(title='Coding', author = self.author, slug='coding', status='1',)
        self.client = Client()
        self.url = reverse('post-create')

    def test_login_requirement(self):
        # Tests that a non-logged-in user is redirected
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
       
    def test_get_post_create(self):
        # Tests that a GET request works and renders the correct template
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

    def test_user_must_be_logged_in(self):
        # Tests that a non-logged in user is redirected
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_form_fields(self):
        # Tests that fields are displayed in the user form
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
