import os
from unittest import TestCase

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.env")))



from src.main.data.model.blog import Blog
from src.main.service.blog_service import BlogService


class TestBlogService(TestCase):
    def setUp(self):
        self.blog_service = BlogService()

    def test_that_a_blog_can_be_added(self):
        blog = Blog("1223344567788", "Jonathan", "My bro")
        result = self.blog_service.add_blog(blog)
        self.assertIsNotNone(result)

    def test_that_i_can_delete_a_blog(self):
        blog = Blog("1223344567788", "Jonathan", "My bro")
        result = self.blog_service.add_blog(blog)
        self.assertIsNotNone(result)
        self.blog_service.delete_blog("1223344567788")
        self.assertIsNotNone(self.blog_service.find_blog("1223344567788"))

