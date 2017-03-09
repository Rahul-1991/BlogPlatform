from app.connections import MySQLConnection


class Config(object):

    VERSIONS_ALLOWED = ['1']
    MYSQL = {
        'host': 'localhost',
        'user': 'root',
        'passwd': 'root',
        'db': 'cv_maindb'
    }
    MYSQL_CONNECTION = MySQLConnection(MYSQL)