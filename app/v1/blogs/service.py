from coordinator import BlogCoordinator


class BlogService(object):

    def __init__(self):
        self.coordinator = BlogCoordinator()

    def get_blog_list(self, pageNo):
        return self.coordinator.blog_list(pageNo)

    def get_blog_content(self, blogId):
        return self.coordinator.blog_content(blogId)

    def add_comment(self, params):
        return self.coordinator.add_comment(params)

    def add_blog(self, params):
        content = params.get('content')
        paragraph_list = content.strip().split('\n\n')
        params.update({'paragraph_list': paragraph_list})
        return self.coordinator.add_blog(params)
