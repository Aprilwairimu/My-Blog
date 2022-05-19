import unittest
from app.models import Blog, User, Comment
from app import db

class TestBlog(unittest.TestCase):

    def setUp(self):
        self.new_blog = Blog(blog_content = "blog one")
        self.new_comment = Comment(comment_content = "One comment", blog=self.new_blog)
    
    def tearDown(self):
        db.session.delete(self)
        User.query.commit()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content,"One comment")
        self.assertEquals(self.new_comment.blog,self.new_blog, 'blog one')