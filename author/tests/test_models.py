from django.test import TestCase
from django.contrib.auth.models import User 
from models import Author
from views import Profile


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



       