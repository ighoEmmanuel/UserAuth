from bson import ObjectId

from src.main.data.model.blog import Blog
from src.main.data.repo.blog_storage import BlogStorage


class BlogService:
    def __init__(self):
        self.storage = BlogStorage()

    def add_blog(self, blog:Blog):
        if blog.author_id is None:
            return {"error":"Field Required"},401
        if blog.title is None:
            return {"error":"Field Required"},401
        if blog.content is None:
            return {"error":"Field Required"},401
        result = self.storage.save_blog(blog)
        blog_id = str(result.inserted_id)
        return{
            "blog_id": blog_id,
            "message": "Blog added successfully",
            "status": 200
        }


    def delete_blog(self, blog_id):
        if not ObjectId.is_valid(blog_id):
            return {"error": "Invalid blog ID"}, 400
        if self.storage.exist_by_blog_id(blog_id):
            self.storage.delete_blog(blog_id)
            return {"message":"Blog deleted successfully"},200
        return {"error":"Blog not found"},404

    def find_blog(self, blog_id):
        if self.storage.exist_by_blog_id(blog_id):
            blog = self.storage.find_blog_by_id(str(blog_id))
            return blog, 200
        return {"error": "Blog not found"}, 404


