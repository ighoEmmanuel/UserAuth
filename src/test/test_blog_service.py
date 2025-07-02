import os
from unittest import TestCase

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(dotenv_path=os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.env")))



from src.main.data.model.blog import Blog
from src.main.service.blog_service import BlogService


class TestBlogService(TestCase):

    def setUp(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["test_db"]

        self.db.users.delete_many({})
        self.db.blogs.delete_many({})

        self.blog_service = BlogService()
        self.blog_service.storage.db = self.db

    def tearDown(self):
        self.db.users.delete_many({})
        self.db.blogs.delete_many({})
        self.client.close()

    def test_that_a_blog_can_be_added(self):
        blog = Blog("122334456778774847954843808", "Jonathan", "My bro")
        result = self.blog_service.add_blog(blog)
        self.assertIsNotNone(result)


    def test_that_i_can_delete_a_blog(self):
        blog = Blog("122334456778774847954843808", "Jonathan", "My bro")
        result = self.blog_service.add_blog(blog)
        self.assertIsNotNone(result)
        self.blog_service.delete_blog(result["blog_id"])
        self.assertIsNotNone(self.blog_service.find_blog(result["blog_id"]))

