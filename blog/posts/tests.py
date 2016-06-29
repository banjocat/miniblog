from django.test import TestCase

from posts.models import Tag, Post

# Create your tests here.
class TagTestCase(TestCase):
    def setup(self):
        pass

    def test_add_tag(self):
        t = Tag(name='c++')
        t.save()
        j = Tag.objects.get(name='c++')
        self.assertEqual(j.name, 'c++')

    def test_add_post(self):
        p = Post(title='Test Post', text='This is a test post')
