from data.model.blog import Blog
from data.repo.blog_storage import BlogStorage


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
        self.storage.save_blog(blog)
        return {"message":"Blog added successfully"},200


    def delete_blog(self, blog_id):
        if self.storage.exist_by_blog_id(blog_id):
            self.storage.delete_blog(blog_id)
            return {"message":"Blog deleted successfully"},200
        return {"error":"Blog not found"},404