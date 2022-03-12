import sqlite3

class SLEEPdatabase:
    def __init__(self, database_src):
        self.database = sqlite3.connect(database_src)
        self.cursr = self.database.cursor()
        self.cursr.execute("""CREATE TABLE IF NOT EXISTS sleep_tracker(
                    datetime_start DATETIME,
                    datetime_end DATETIME,
                    duration TIME
                )""")
        self.cursr.execute("""CREATE TABLE IF NOT EXISTS sleep_plans(
                    datetime_start DATETIME,
                    datetime_end DATETIME,
                    duration TIME
                )""")
        self.database.commit()

    def insert_tracker(self, datetime_start, datetime_end, duration):
        self.cursr.execute("INSERT INTO sleep_tracker values (NULL, ?, ?, ?)",
                            (datetime_start, datetime_end, duration))
        self.database.commit()

    def insert_plans(self, datetime_start, datetime_end, duration):
        self.cursr.execute("INSERT INTO sleep_plans values (NULL, ?, ?, ?)",
                            (datetime_start, datetime_end, duration))
        self.database.commit()
    
    def fetch_tracker(self):
        self.cursr.execute("SELECT rowid, * FROM sleep_tracker")
        return self.cursr.fetchall()
    
    def fetch_plans(self):
        self.cursr.execute("SELECT rowid, * FROM sleep_plans")
        return self.cursr.fetchall()
    
    def remove_tracker(self):
        self.cursr.execute("DELETE FROM sleep_tracker WHERE id=?", (id,))
        self.database.commit()

    def remove_plans(self):
        self.cursr.execute("DELETE FROM sleep_plans WHERE id=?", (id,))
        self.database.commit()

    def update_tracker(self, id, datetime_start, datetime_end, duration):
        self.cursr.execute("UPDATE sleep_tracker SET datetime_start = ?, datetime_end = ?, duration = ? WHERE id = ?",
                            (datetime_start, datetime_end, duration, id))
        self.database.commit()
    
    def update_plans(self, id, datetime_start, datetime_end, duration):
        self.cursr.execute("UPDATE sleep_plans SET datetime_start = ?, datetime_end = ?, duration = ? WHERE id = ?",
                            (datetime_start, datetime_end, duration, id))
        self.database.commit()
