from config import Config


class BlogCoordinator(object):

    def __init__(self):
        self.mysql_conn = Config.MYSQL_CONNECTION

    def blog_list(self, pageNo):
        query = 'select * from blog'
        result = self.mysql_conn.query_db(query)
        start, end = (int(pageNo)-1)*5, int(pageNo)*5
        return result[start: end] if result[start: end] else result[0: 5]

    def get_paragraph_id_list(self, block_id):
        query = 'select paragraph_id from paragraph where block_id = ("%s")' % (block_id)
        result = self.mysql_conn.query_db(query)
        return map(lambda x: str(x.get('paragraph_id')), result)

    def get_blog_title(self, blog_id):
        query = 'select * from blog where blog_id = ("%s")' % blog_id
        result = self.mysql_conn.query_db(query)
        return result[0].get('title')

    def get_paragraphs(self, blog_id):
        query = 'select content from paragraph where block_id = ("%s")' % blog_id
        result = self.mysql_conn.query_db(query)
        return '\n\n'.join(map(lambda x: x.get('content'), result))

    def get_all_comments(self, paragraph_id_list):
        query = 'select paragraph_id, content from comments where paragraph_id in (%s)' % ','.join(paragraph_id_list)
        result = self.mysql_conn.query_db(query)
        return list(result)

    def blog_content(self, blogId):
        title = self.get_blog_title(blogId)
        content = self.get_paragraphs(blogId)
        paragraph_id_list = self.get_paragraph_id_list(blogId)
        comments_list = self.get_all_comments(paragraph_id_list)
        return {
            'blog_id': blogId,
            'title': title,
            'content': content,
            'comments': comments_list
        }

    def add_comment(self, params):
        blog_id = params.get('blogId')
        paragraph_id = params.get('paragraphId')
        content = params.get('content')
        query = 'insert into comments (paragraph_id, content) values ("%s", "%s")' % (paragraph_id, content)
        self.mysql_conn.write_db(query)
        return {}

    def get_paragraph_list(self, content):
        return content.strip().split('&')

    def get_block_id(self, title):
        query = 'select blog_id from blog where title = "%s"' % title
        result = self.mysql_conn.query_db(query)
        return result[0].get('blog_id')

    def add_blog(self, params):
        query = 'insert into blog (title) values ("%s")' % params.get('title')
        self.mysql_conn.write_db(query)
        block_id = self.get_block_id(params.get('title'))
        paragraph_list = self.get_paragraph_list(params.get('content'))
        for paragraph in paragraph_list:
            query = "insert into paragraph (block_id, content) values ('%s', '%s')" % (block_id, paragraph)
            self.mysql_conn.write_db(query)
        return {}

