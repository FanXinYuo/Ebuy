from Ebuy.DataBase.ConnectDatabase import Mysql


class DatabaseExecute(Mysql):
    def selectdate(self, sql):
        cursor = self.db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def commit(self):
        self.db.commit()
