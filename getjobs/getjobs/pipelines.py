from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
from pathlib import Path
from urllib import parse
from dotenv import load_dotenv
from os import path
from itemadapter import ItemAdapter

user_mssql = os.getenv('serveruser')
password_mssql = os.getenv('serverpassword')
database_mssql = os.getenv('serverdatabase')
host_mssql = os.getenv('serverhost')


def mssql_jobs():
    connection_url = URL.create(
            "mssql+pyodbc",
            username=f"{user_mssql}",
            password=f"{password_mssql}",
            host=f"{host_mssql}",
            database=f"{database_mssql}",
            query={
                "driver": "ODBC Driver 17 for SQL Server",
                "autocommit": "True",
        }
        )
      
    engine = create_engine(connection_url).execution_options(
    isolation_level="AUTOCOMMIT", future=True,fast_executemany=True)
    return engine

class GetjobsPipeline:
    def process_item(self, item, spider):
        return item
    
    def authentication(self, *args, **kwargs):
        ...
    
    def inserts(self, *args, **kwargs):
        ...
        
    def update(self, *args, **kwargs):
        ...
        
    def delete(self, *args, **kwargs):
        ...
