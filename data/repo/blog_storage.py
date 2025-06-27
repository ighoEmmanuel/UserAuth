import os

from flask import Flask
from flask_pymongo import PyMongo

from data.model.blog import Blog


app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URL").strip()
mongo = PyMongo(app)


class BlogStorage:
    def __init__(self):
        self.db = mongo.db


    def save_blog(self, blog:Blog):
        blog_item = blog.to_dict()
        return self.db.blogs.insert_one(blog_item)

    def find_blog_by_id(self, blog_id:int):
        return self.db.blogs.find_one({"_id": blog_id})


    def delete_blog(self, blog_id:int):
        return self.db.blogs.delete_one({"_id": blog_id})


    def exist_by_blog_id(self, blog_id) -> bool:
        return self.db.blogs.find_one({"_id": blog_id})