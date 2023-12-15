from django.test import TestCase, Client
from django.contrib.auth.models import User 
from app.models import Profile, Author, Category, Tag, Post, Comment, Contact
from django.urls import reverse


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
        self.user = User.objects.create_user(username='avatar', id=1)
        self.hacker = User.objects.create_user(username='hacker')
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile)
        self.post= Post.objects.create(title='Karramba', author = self.author, slug='karramba',status='1')
        self.comment= Comment.objects.create(body='it is a comment', author = self.user, post=self.post)
        self.client = Client()
        self.url = reverse('post-detail', args=['karramba'])

    
    def test_get_post_detail(self):
        """ Tests that a GET request works and renders the correct template"""
        
        response = self.client.get(self.url)
    
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/post_detail.html')



class TestDeletePost(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='avatar', id=1)
        self.hacker = User.objects.create_user(username='hacker')
        self.profile = Profile.objects.get(user=self.user) 
        self.author = Author.objects.create(profile=self.profile)
        self.post= Post.objects.create(title='Karramba', author = self.author, slug='karramba',status='1')
        self.post.save()
        self.client = Client()
        self.url = reverse('post_detail', args=[str(self.id)])

    # def test_login_requirement(self):
    #     """ Tests a non-logged in user gets a 404 """

    #     response = self.client.get(self.url)

    #     self.assertEqual(response.status_code, 404)

    # def test_author_gets_200(self):
    #     """ Tests that the logged in author gets a 200 response """

    #     self.client.force_login(self.user)
    #     response = self.client.get(self.url)

    #     self.assertEqual(response.status_code, 200)

    # def test_nonauthor_gets_404(self):
    #     """ Tests that a logged in user who is not the author gets a 404 """

    #     self.client.force_login(self.hacker)
    #     response = self.client.get(self.url)

    #     self.assertEqual(response.status_code, 404)


        