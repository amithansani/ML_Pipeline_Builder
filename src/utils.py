import sqlite3
import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logger import logging
from src.exception import CustomException

class DatabaseExecutions:
    def __init__(self,dbname="database/MLPipeline"):
        self.conn=sqlite3.connect(dbname)
        self.cursor=self.conn.cursor()
    # def create_db_connector(dbname):
    #     conn=sqlite3.connect("database/MLPipeline")
    #     # cursor = conn.cursor()
    #     return conn

    def execute_ddl_dml(self,query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except Exception as e:
            CustomException(e,sys)
    def get_columns(self,table_name):
        return [rows[1] for rows in self.cursor.execute(f'''PRAGMA table_info({table_name})''')]
        
    def execute_query(self,query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()


            column_names = [description[0] for description in self.cursor.description]


            return pd.DataFrame(rows, columns=column_names)
        except Exception as e:
            CustomException(e,sys)
        
    def close_connection(self):
        self.conn.close()

    
