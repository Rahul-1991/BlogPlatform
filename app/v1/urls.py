from flask import Blueprint
from blogs import views as blog_views

v1 = Blueprint('v1', __name__)

# # blog urls
blog_prefix = '/blogs'

v1.add_url_rule(blog_prefix + '/listBlogs',
                view_func=blog_views.ListBlogs.as_view('list_blogs'))
v1.add_url_rule(blog_prefix + '/blogDescription',
                view_func=blog_views.BlogDescription.as_view('blog_description'))
v1.add_url_rule(blog_prefix + '/addComment',
                view_func=blog_views.AddComment.as_view('add_comment'))
v1.add_url_rule(blog_prefix + '/addBlog',
                view_func=blog_views.AddBlog.as_view('add_blog'))

