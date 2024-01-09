from django.test import TestCase
from django.contrib.auth.models import User
from author.models import Author
from profile.models import Profile
from author.forms import AuthorMessage, AuthorAccessRequest
from blog.models import Post, Comment, Category, Tag
from profile.models import Contact


class ProfileModelTest(TestCase):
    """
    Test suite for the Profile model.
    """

    def setUp(self):
        """
        Set up function to create a user and associated profile for testing.
        """
        self.user = User.objects.create_user(username='avatar', id=1)
        self.profile = Profile.objects.get(user=self.user)

    def test_create_profile(self):
        """
        Test to ensure a profile is successfully created for a user.
        """
        self.assertTrue(self.profile)

    def test_profile_str(self):
        """
        Test the string representation of the Profile model.
        """
        self.assertEqual(str(self.profile), self.user.username)

    def test_get_absolute_url_for_profile(self):
        """
        Test the get_absolute_url method of the Profile model.
        """
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.get_absolute_url(), '/profile/1/')


class AuthorModelTest(TestCase):
    """
    Test suite for the Author model.
    """

    def setUp(self):
        """
        Set up function to create a user and associated author for testing.
        """
        self.user = User.objects.create_user(username='avatar', id=1)
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)

    def test_create_author(self):
        """
        Test to ensure an author is successfully created.
        """
        self.assertTrue(self.author)

    def test_author_str(self):
        """
        Test the string representation of the Author model.
        """
        self.assertEqual(str(self.author), self.profile.user.username)


class AuthorMessageModelTest(TestCase):
    """
    Test suite for the AuthorMessage model.
    """

    def test_author_message_str_representation(self):
        """
        Test to ensure the string representation of the AuthorMessage model
        is as expected.
        """
        user = User.objects.create_user(
            username='testuser', password='testpassword')
        author_message = AuthorMessage(
            author=user, sender_name="John Doe",
            sender_email="john@example.com",
            message="Hello, I'm a fan of your work!"
        )
        str_representation = str(author_message)
        expected_str = "Message from John Doe to testuser"
        self.assertEqual(str_representation, expected_str)


class AuthorAccessRequestModelTest(TestCase):
    """
    Test suite for the AuthorAccessRequest model.
    """

    def test_author_access_request_str_representation(self):
        """
        Test to ensure the string representation of the AuthorAccessRequest model
        is as expected.
        """
        user = User.objects.create_user(
            username='testuser', password='testpassword')
        author_access_request = AuthorAccessRequest(
            profile=user.profile,
            request_reason="I want to access exclusive content."
        )
        str_representation = str(author_access_request)
        expected_str = "Request from testuser"
        self.assertEqual(str_representation, expected_str)


class CategoryModelTest(TestCase):
    """
    Test suite for the Category model in the blog app.
    """

    def setUp(self):
        """
        Set up function to create a category instance for testing.
        """
        self.category = Category.objects.create(title='News', slug='news')

    def test_create_category(self):
        """Tests that a category instance can be created."""
        self.assertTrue(self.category)

    def test_category_str(self):
        """Tests the string representation (__str__) of the Category model."""
        title = Category.objects.get(title=self.category.title)
        self.assertEqual(str(title), 'News')


class TagModelTest(TestCase):
    """
    Test suite for the Tag model in the blog app.
    """

    def setUp(self):
        """
        Set up function to create a tag instance for testing.
        """
        self.tag = Tag.objects.create(name='tag', slug='post comment')

    def test_create_tag(self):
        """
        Tests that a tag instance can be created.
        """
        self.assertTrue(self.tag)

    def test_tag_str(self):
        """
        Tests the string representation (__str__) of the Tag model.
        """
        name = Tag.objects.get(name=self.tag.name)
        self.assertEqual(str(name), 'tag')


class PostModelTest(TestCase):
    """
    Test suite for the Post model in the blog app.
    """

    def setUp(self):
        """
        Set up function to create a user, profile, author, and post instance for testing.
        """
        self.user = User.objects.create_user(username='avatar', id=1)
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)
        self.post = Post.objects.create(
            title='Karramba', author=self.author, slug='karramba')

    def test_create_post(self):
        """
        Tests that a post instance can be created.
        """
        self.assertTrue(self.post)

    def test_post_title(self):
        """
        Tests the string representation (__str__) of the Post model.
        """
        self.assertEqual(str(self.post), 'Karramba')

    def test_creates_a_slug(self):
        """
        Tests that a slug is automatically created for the post.
        """
        self.assertEqual(self.post.slug, 'karramba')

    def test_slugs_are_unique(self):
        """
        Tests that slugs are unique for different posts.
        """
        second_post = Post.objects.create(
            title='My blog post', author=self.author)
        self.assertNotEqual(self.post.slug, second_post.slug)

    def test_get_absolute_url_for_post(self):
        """
        Tests the get_absolute_url method of the Post model.
        """
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/post/1/')


class CommentModelTest(TestCase):
    """
    Test suite for the Comment model in the blog app.
    """

    def setUp(self):
        """
        Set up function to create a user, profile, author, post, and comment instance for testing.
        """
        self.user = User.objects.create_user(username='avatar', id=1)
        self.profile = Profile.objects.get(user=self.user)
        self.author = Author.objects.create(profile=self.profile)
        self.post = Post.objects.create(
            title='Karramba', author=self.author, slug='karramba')
        self.comment = Comment.objects.create(
            post=self.post, author=self.user, name='Comment',
            body='Its a comment body', approved=True)

    def test_create_comment(self):
        """
        Tests that a comment instance can be created.
        """
        self.assertTrue(self.comment)

    def test_comment_return_str(self):
        """
        Tests the string representation (__str__) of the Comment model.
        """
        expected_str = f"Comment {self.comment.body} by {self.comment.name}"
        self.assertEqual(str(self.comment), expected_str)

    def test_comment_approved_comments(self):
        """
        Tests that the 'approved' attribute of the Comment model works as expected.
        """
        self.assertTrue(self.comment.approved)


class ContactModelTest(TestCase):
    """
    Test suite for the Contact model in the profile app.
    """

    def setUp(self):
        """
        Set up function to create a contact instance for testing.
        """
        self.contact = Contact.objects.create(
            email='user@gmail.com', message='i need to contact u',
            name='randomperson')

    def test_create_contact(self):
        """
        Tests that a contact instance can be created.
        """
        self.assertTrue(self.contact)

    def test_contact_return_str(self):
        """
        Tests the string representation (__str__) of the Contact model.
        """
        email = Contact.objects.get(email=self.contact.email)
        self.assertEqual(str(email), 'user@gmail.com')
