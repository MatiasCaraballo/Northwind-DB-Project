
import sqlite3

''' Connection to the database'''
class connection:
    
    def __init__(self, db_path='Northwind.db'):
        self._conn = sqlite3.connect(db_path)

    def get_connection(self):
        return self._conn

    def cursor(self):
        return self._conn.cursor()

    def close(self):
        self._conn.close()

    def __enter__(self):
        return self

    