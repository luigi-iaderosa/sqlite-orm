import sqlite3

class SqliteOp:

    def __init__(self,dbAddress):
        # dbAddress is something like '/home/alceste/litedbs/bookstack'
        self.conn = sqlite3.connect(dbAddress)

    def executeQuery(self, edit, sql, args=[]):
        cursor = self.conn.cursor()
        cursor.execute(sql, args)

        if edit == True:
            data = self.conn.commit()
        else:
            data = cursor.fetchall()
        self.conn.close()
        return data

    def executeDBInterrogation(self, sql, args=[]):
        return self.executeQuery(False, sql, args)

    def executeDBEdit(self, sql, args=[]):
        return self.executeQuery(True, sql, args)
