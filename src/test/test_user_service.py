from unittest import TestCase

from pymongo import MongoClient

from src.main.data.model.blog import Blog
from src.main.data.model.user import User
from src.main.service.user_service import UserService


class TestUserService(TestCase):

    def setUp(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["test_db"]


        self.db.users.delete_many({})
        self.db.blogs.delete_many({})

        self.user_service = UserService()
        self.user_service.storage.db = self.db

    def tearDown(self):
        self.db.users.delete_many({})
        self.db.blogs.delete_many({})
        self.client.close()

    def test_that_a_can_add_post(self):
        user = User("Emmanuel", "lase@gmail.com", "fatter")
        response, status = self.user_service.register(user)
        token = response
        from src.main.security.jwt_utils import verify_token
        user_id = verify_token(token)
        blog = Blog(user_id, "Jonathan", "My bro")
        result = self.user_service.add_post(blog)
        self.assertIsNotNone(result)


    def test_that_a_user_can_delete_blog(self):
        user = User("Emmanuel", "ase@gmail.com", "fatter")
        response, status = self.user_service.register(user)
        token = response['token']
        from src.main.security.jwt_utils import verify_token
        user_id = verify_token(token)
        blog = Blog(user_id, "Jonathan", "My bro")
        result = self.user_service.add_post(blog)
        self.user_service.delete_post(result["blog_id"])
        self.assertEqual(0,len(self.user_service.get_user_blogs(user_id)))


