import mysql.connector

class DbConnector:

    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.conn = None
        self.cursor = None

    def connect(self):
        if self.conn is None or not self.conn.is_connected():
            self.conn = mysql.connector.connect(
                host=self.host,    
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
                
    def execute(self, query: str, params=None):
        if not self.cursor:
            raise Exception("Cursor is not initialized. Call connect() first.")
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def __del__(self):
        try:
            if self.cursor:
                self.cursor.close()
        except Exception:
            pass
        try:
            if self.conn:
                self.conn.close()
        except Exception:
            pass