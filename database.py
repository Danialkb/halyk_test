import os
from typing import Protocol

import psycopg2
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('HOST')
database = os.getenv('DATABASE')
user = os.getenv('USER')
password = os.getenv('PASSWORD')

# print(host, database, user, password)

db_config = {
    'user': user,
    'host': host,
    'port': 5433,
    'database': database,
    'password': password
}


class Database(Protocol):

    def save_pdf_data(self, pdf_name: str, data: str): ...


class DatabasePostgres:
    def __init__(self, db_config: dict):
        self.db_config = db_config

    def save_pdf_data(self, pdf_name: str, data: str):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute(f'INSERT INTO public.pdf_db (pdf_name, pdf_body) VALUES (%s, %s)', (pdf_name, data))

        conn.commit()
        cursor.close()
        conn.close()

    def _connect(self):
        conn = psycopg2.connect(
            host=self.db_config.get('host'),
            port=self.db_config.get('port'),
            database=self.db_config.get('database'),
            user=self.db_config.get('user'),
            password=self.db_config.get('password')
        )

        return conn


def db_setup() -> Database:

    return DatabasePostgres(db_config=db_config)
