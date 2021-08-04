import pymysql


class Mysql:
    ip = ''
    username = ''
    password = ''
    database = ''
    db = ''

    def __init__(self, ip, username, password, database):
        self.ip = ip
        self.username = username
        self.password = password
        self.database = database
        self.db = pymysql.connect(self.ip, self.username, self.password, self.database)
