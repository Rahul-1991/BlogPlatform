from flask.views import MethodView
from app.decorators import process_params
from app.common_utils import get_success_response
from service import BlogService


class ListBlogs(MethodView):

    param_config = {
        'type': 'object',
        'properties': {
            'pageNo': {
                'type': 'string'
            }
        },
        'required': ['pageNo']
    }

    @process_params(param_config=param_config)
    def get(self, params):
        pageNo = params.get('pageNo')
        result = BlogService().get_blog_list(pageNo)
        return get_success_response(1, 'blog_list', result)


class BlogDescription(MethodView):

    param_config = {
        'type': 'object',
        'properties': {
            'blogIdentifier': {
                'type': 'string'
            }
        },
        'required': ['blogIdentifier']
    }

    @process_params(param_config=param_config)
    def get(self, params):
        blogId = params.get('blogIdentifier')
        result = BlogService().get_blog_content(blogId)
        return get_success_response(1, 'blog_content', result)


class AddComment(MethodView):

    param_config = {
        'type': 'object',
        'properties': {
            'blogId': {
                'type': 'string'
            },
            'paragraphId': {
                'type': 'string'
            },
            'content': {
                'type': 'string'
            }
        }
    }

    @process_params(param_config=param_config)
    def post(self, params):
        result = BlogService().add_comment(params)
        return get_success_response(1, 'Comment Added Successfully', result)


class AddBlog(MethodView):

    param_config = {
        'type': 'object',
        'properties': {
            'title': {
                'type': 'string'
            },
            'content': {
                'type': 'string'
            }
        },
        'required': ['title', 'content']
    }

    @process_params(param_config=param_config)
    def post(self, params):
        result = BlogService().add_blog(params)
        return get_success_response(1, 'Blog Added Successfully', result)