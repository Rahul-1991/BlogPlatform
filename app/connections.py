import MySQLdb


class MySQLConnection(object):
    def __init__(self, db_config):
        self.db_config = db_config
        try:
            self.connection = MySQLdb.connect(**self.db_config)
            self.cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        except Exception as e:
            self.connection.close()

    def query_db(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def write_db(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
