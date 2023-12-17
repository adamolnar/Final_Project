from django.test import TestCase, Client
from django.contrib.auth.models import User 
from app.models import Profile, Author, Category, Tag, Post, Comment, Contact
from app.forms import ContactForm
from django.urls import reverse
from django.contrib.messages import get_messages


class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hemingway', id=1, email='user@gmail.com',password='1234'
        )
        self.profile = Profile.objects.get(user=self.user) 
        self.client = Client()
        self.url = reverse('profile', args=['1'])
        self.response = self.client.get(self.url)

    def test_user_must_be_logged_in(self):        
        """ Tests that a non-logged in user is redirected to login page""" 
        response = self.client.get(self.url)  
        self.assertEqual(response.status_code, 302)

    def test_returns_200(self):
        """ Tests correctly logged in user response"""
        self.client.login(username='hemingway', password="1234")
        response = self.client.get(reverse("profile", kwargs=({"pk": self.user.pk})))
        self.assertEqual(response.status_code, 200)
 
    def test_get_add(self):        
        """ Tests that a GET request works and renders the correct template"""         
        self.client.force_login(self.user)        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/profile.html')

    def test_view_returns_profile_of_current_user(self):
        """Check the profile of the current user"""
        self.client.login(username='hemingway', password="1234")
        response = self.client.get(reverse("profile",kwargs=({"pk": self.user.pk})))
        self.assertEqual(response.context["user"], self.user)
        self.assertEqual(response.context["profile"], self.user.profile)



class ProfileUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hemingway',  email='user@gmail.com',password='1234', id='1')
        self.profile = Profile.objects.get(user=self.user) 

    def test_edit_profile_returns_200(self):
        """Check the profile update belongs to current user"""
        self.client.login(username='hemingway', password='1234')
        response = self.client.get(reverse('profile-update', args=['1']))
        self.assertEqual(response.status_code, 200)



class AuthorListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='hemingway', id=1, email='user@gmail.com',password='1234')
        self.profile = Profile.objects.get(user=self.user) 
        """Create 13 authors for pagination tests"""
        number_of_authors = 13

        for profile in range(number_of_authors):
            Author.objects.create(
                profile=self.profile,
            ) 

    def test_view_uses_correct_template(self):
        """Test that authors list is using correct template"""
        response = self.client.get('/authors/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/authors_list.html')

    def test_view_url_accessible_by_name(self):
        """Test if authors list can be accesses by authors name"""
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_ten(self):
        """Get first page and confirm it has (exactly) remaining 10 items"""
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['author_list']), 10)

    def test_lists_all_authors(self):
        """Get second page and confirm it has (exactly) remaining 3 items"""
        response = self.client.get(reverse('authors-list')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['author_list']), 3)


class AuthorDetailViewTestCase(TestCase):

    def setUp(self):
        # Set up any necessary data before running the tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile)


    def test_author_detail_view_with_valid_author(self):
        # Test the AuthorDetailView with a valid author
        response = self.client.get(reverse('author-detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/author_detail.html')  # Check if the correct template is used
        self.assertEqual(response.context['author_info'], self.author)  # Check if the author_info context variable is set

    def test_author_detail_view_with_invalid_author(self):
        # Test the AuthorDetailView with an invalid author
        invalid_author_pk = self.author.pk + 1  # Assuming the next primary key is invalid
        response = self.client.get(reverse('author-detail', args=[invalid_author_pk]))
        self.assertEqual(response.status_code, 404)  # Expecting a 404 Not Found response

    def test_author_detail_view_with_no_posts(self):
        # Test the AuthorDetailView for an author with no posts
        response = self.client.get(reverse('author-detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], [])  # Check if the post_list context variable is an empty queryset

    def test_author_detail_view_with_posts(self):
        # Test the AuthorDetailView for an author with posts
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)
        response = self.client.get(reverse('author-detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], [repr(post)])  # Check if the post_list context variable contains the expected post



class TestIndexView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='avatar', id=1)
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile)
        self.post= Post.objects.create(title='Karramba', author = self.author, slug='karramba',status='1',)
        self.post1= Post.objects.create(title='News', author = self.author, slug='news')
        self.post2= Post.objects.create(title='Coding', author = self.author, slug='coding', status='1',)
        self.response = Client().get(reverse('index'))

    def test_get_index(self):
        """ Tests that a get request to index works and renders the correct template"""

        self.assertEquals(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'app/index.html')

    def test_context_contains_posts(self):
        """ Tests that there the context contains 'post_list' """

        self.assertIn('post_list', self.response.context)

    def test_excludes_draft_posts(self):
        """ Tests that the list of posts on the homepage excludes drafts"""

        number_of_published_posts = len(self.response.context['post_list'])

        self.assertEqual(number_of_published_posts,2)



class TestAddPostView(TestCase):

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
        """ Tests that a non-logged-in user is redirected """

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
       

    def test_get_post_create(self):
        """ Tests that a GET request works and renders the correct template"""

        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/post_form.html')

    def test_user_must_be_logged_in(self):
        """ Tests that a non-logged in user is redirected """

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)

    def test_form_fields(self):
        """ Tests that fields are displayed in the user form"""

        self.client.force_login(self.user)
        response = self.client.get(self.url)
        form = response.context_data['form']

        self.assertEqual(len(form.fields), 6)
        self.assertIn('title', form.fields)
        self.assertIn('content', form.fields)
        self.assertIn('featured_image', form.fields)
        self.assertIn('status', form.fields)
        self.assertIn('categories', form.fields)
        self.assertIn('tags', form.fields)

class TestPostDetailView(TestCase):

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
        self.assertTemplateUsed(response, 'app/post_detail.html')
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
        
class TestPostLikeView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)

    def test_post_like(self):
        url = reverse('post-like', kwargs={'slug': self.post.slug})
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after liking a post
        self.post.refresh_from_db()
        self.assertTrue(self.user in self.post.likes.all())

    def test_post_unlike(self):
        url = reverse('post-like', kwargs={'slug': self.post.slug})
        self.client.login(username='testuser', password='testpassword')
        self.post.likes.add(self.user)  # Simulate the user has already liked the post

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after unliking a post
        self.post.refresh_from_db()
        self.assertFalse(self.user in self.post.likes.all())


class TestPostCreateView(TestCase):

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

    def setUp(self):
        # Create a user, profile, and author
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)

        # Create a post
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)

    def test_post_update_view(self):
        url = reverse('post-update', kwargs={'slug': self.post.slug})
        self.client.login(username='testuser', password='testpassword')

        data = {
            'title': 'Updated Post Title',
            'content': 'Updated Content',
            'featured_image': 'path/to/updated/image.jpg',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after updating a post

        updated_post = Post.objects.get(id=self.post.id)
        self.assertEqual(updated_post.title, 'Updated Post Title')
        self.assertEqual(updated_post.content, 'Updated Content')
       
class TestPostDeleteView(TestCase):

    def setUp(self):
        # Create a user, profile, and author
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)

        # Create a post
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)

    def test_post_delete_view(self):
        url = reverse('post-delete', kwargs={'slug': self.post.slug})
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after deleting a post

        # Ensure that the post has been deleted
        with self.assertRaises(Post.DoesNotExist):
            deleted_post = Post.objects.get(id=self.post.id)

class CommentUpdateViewTest(TestCase):

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


    def test_comment_update_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Get the template for the CommentUpdateView
        self.assertTemplateUsed('app/comment_update.html')
        
        # Simulate a GET request to the CommentUpdateView
        url = reverse('comment-update', kwargs={'pk': self.comment.pk})
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Simulate a POST request to update the comment
        updated_body = 'Updated Comment Body'
        response = self.client.post(url, {'body': updated_body})

        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the comment was updated in the database
        updated_comment = Comment.objects.get(pk=self.comment.pk)
        self.assertEqual(updated_comment.body, updated_body)

        # Check that the user is redirected to the expected URL after updating the comment
        expected_redirect_url = reverse('index') 
        self.assertRedirects(response, expected_redirect_url)


class CommentDeleteViewTest(TestCase):

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

        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

    def test_comment_delete_view(self):
        # Get the URL for the CommentDeleteView
        url = reverse('comment-delete', kwargs={'pk': self.comment.pk})

        # Simulate a GET request to the CommentDeleteView
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the comment is present in the response context
        self.assertEqual(response.context['comment'], self.comment)

        # Simulate a POST request to delete the comment
        response = self.client.post(url)

        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the comment is deleted from the database
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(pk=self.comment.pk)

        # Check that a success message is present in the messages framework
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'The comment has been deleted successfully.')

        # Check that the user is redirected to the expected URL after deleting the comment
        expected_redirect_url = reverse('index')  # Replace 'index' with the actual URL name
        self.assertRedirects(response, expected_redirect_url)


class ContactViewTest(TestCase):
    def test_contact_view_get(self):
        client = Client()
        response = client.get(reverse('contact'))  # Replace 'contact' with the actual URL name

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'app/contact.html')

        # Check that the form is present in the context
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contact_view_post_valid(self):
        client = Client()
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message content',
        }
        response = client.post(reverse('contact'), data)  # Replace 'contact' with the actual URL name

        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the user is redirected to the 'success' page
        self.assertRedirects(response, reverse('success'))  # Replace 'success' with the actual URL name

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
        self.assertTemplateUsed(response, 'app/contact.html')

        # Check that the form is present in the context
        self.assertIsInstance(response.context['form'], ContactForm)

        # Check that the form has errors
        self.assertTrue(response.context['form'].errors)

