from django.test import TestCase
from django.contrib.auth.models import User 
from models import Profile, Author, Post


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
        self.assertTemplateUsed(response, 'app/authors_list.html')

    def test_view_url_accessible_by_name(self):
        # Test if authors list can be accesses by authors name
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_ten(self):
        # Get first page and confirm it has (exactly) remaining 10 items
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['author_list']), 10)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 4 items
        response = self.client.get(reverse('authors-list')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['author_list']), 4)


class AuthorDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        self.user = User.objects.create_user(username='hemingway', id=1, email='user@gmail.com',password='1234')
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile)

    def test_author_detail_view_with_valid_author(self):
        # Test the AuthorDetailView with a valid author
        response = self.client.get(reverse('author-detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/author_detail.html')  
        self.assertEqual(response.context['author_info'], self.author) 

    def test_author_detail_view_with_invalid_author(self):
        # Test the AuthorDetailView with an invalid author
        invalid_author_pk = self.author.pk + 1 
        response = self.client.get(reverse('author-detail', args=[invalid_author_pk]))
        self.assertEqual(response.status_code, 404) 

    def test_author_detail_view_with_no_posts(self):
        # Test the AuthorDetailView for an author with no posts
        response = self.client.get(reverse('author-detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], [])  

    def test_author_detail_view_with_posts(self):
        # Test the AuthorDetailView for an author with posts
        post = Post.objects.create(title='Test Post', content='Test Content', author=self.author, status=1)
        response = self.client.get(reverse('author-detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], [repr(post)])  



    
