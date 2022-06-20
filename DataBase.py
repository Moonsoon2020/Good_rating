import sqlite3


class ControlDB:
    def __init__(self):
        self.con = sqlite3.connect('db_for_data.db', check_same_thread=False)  # подключение БД
        tabl = '''CREATE TABLE  IF NOT EXISTS date (
                  login,
                  password);'''
        self.con.cursor().execute(tabl)
        self.con.commit()

    def add(self, login, password):
        self.con.cursor().execute(
            f'''INSERT INTO date (login, password) VALUES ('{login}', '{password}')''')
        self.con.commit()

    def delete(self):
        self.con.cursor().execute(f'''DELETE from date''')
        self.con.commit()

    def get(self):
        return self.con.cursor().execute(f'''SELECT login, password FROM date''').fetchall()

# c = ControlDB()
# c.add('l', 'u')
# print(c.get())
# c.delete()
