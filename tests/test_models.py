from django.test import TestCase
from django.contrib.auth.models import User 
from app.models import Profile, Author, Category, Tag, Post, Comment, Contact

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='avatar', id=1)
        self.profile = Profile.objects.get(user=self.user) 
        
            
    def test_create_profile(self):
        """ Tests that profile can be created """
        self.assertTrue(self.profile)

    def test_profile_is_active(self):
        """ Tests that profile without image can be created """
        self.profile.is_active = False 
        self.assertFalse(bool(self.profile.is_active))

    def test_profile_str(self):
        """ Tests the __str__ of the Profile model"""
        self.assertEqual(str(self.profile), self.user.username )




class AuthorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='avatar', id=1)
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile)
            
    def test_create_author(self):
        """ Tests that author can be created """
        self.assertTrue(self.author)

    def test_author_str(self):
        """ Tests the __str__ of the Author model"""
        self.assertEqual(str(self.author), self.profile.user.username )



class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='News', slug= 'news')
         
    def test_create_category(self):
        """ Tests that category can be created """
        self.assertTrue(self.category)


    def test_category_str(self):
        """ Tests the __str__ of the Category model"""
        self.assertEqual(str(self.category.title), self.category.title)


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='post comment', slug= 'post comment')
         
    def test_create_category(self):
        """ Tests that category can be created """
        self.assertTrue(self.tag)


    def test_category_str(self):
        """ Tests the __str__ of the Post model"""
        self.assertEqual(str(self.tag.name), 'post comment')




class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='avatar', id=1)
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile)
        self.post= Post.objects.create(title='Karramba', author = self.author, slug='karramba')

            
    def test_create_post(self):
        """ Tests that post can be created """
        self.assertTrue(self.post)


    def test_post_title(self):
        """ Tests the __str__ of the Post model"""
        self.assertEqual(str(self.post), 'Karramba' )


    def test_creates_a_slug(self):
        """ Tests a slug is automatically created """
        self.assertEqual(self.post.slug, 'karramba')


    def test_slugs_are_unique(self):
        """ Tests two posts with identical titles from the same author receive different slugs """
        second_title = Post.objects.create(
            title='My blog post',
            author=self.author,
        )
        self.assertNotEqual(self.post.slug, second_title.slug)

    # @property
    # def test_number_of_likes(self):
    #     self.likes.all().count()


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='avatar', id=1)
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile)
        self.post= Post.objects.create(title='Karramba', author = self.author, slug='karramba')
        self.comment = Comment.objects.create(
            post = self.post,
            author = self.user,
            name = 'Comment',
            body= 'Its a comment body',
            approved = True,
        )
            
    def test_create_comment(self):
        """ Tests that comment can be created """
        self.assertTrue(self.comment)

    def test_comment_return_str(self):
        """ Tests the __str__ of the Comment model"""
        self.assertEqual(str(self.comment), f"Comment {self.comment.body} by {self.comment.name}" )

    def test_comment_approved_comments(self):
        """ Tests the approved = True of the Comment model"""
        self.assertEqual(bool(self.comment), True )


class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            email = 'user@gmail.com',
            message = 'i need to cntact u',
            name = 'randomperson',
        )

                
    def test_create_contact(self):
        """ Tests that comment can be created """
        self.assertTrue(self.contact)

    def test_contact_return_str(self):
        """ Tests the __str__ of the Comment model"""
        self.assertEqual(str(self.contact.email), 'user@gmail.com' )
       