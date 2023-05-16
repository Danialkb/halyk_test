import os

import psycopg2
from dotenv import load_dotenv


class DatabasePostgres:
    def __init__(self, db_config: dict):
        self.db_config = db_config

    def save_pdf_data(self, pdf_name: str, data: str):
        print(self.db_config)
        conn = psycopg2.connect(
            host=self.db_config.get('host'),
            port=self.db_config.get('port'),
            database=self.db_config.get('database'),
            user=self.db_config.get('user'),
            password=self.db_config.get('password')
        )
        cursor = conn.cursor()

        cursor.execute(f'INSERT INTO public.pdf_db (pdf_name, pdf_body) VALUES (%s, %s)', (pdf_name, data))

        conn.commit()
        cursor.close()
        conn.close()


def db_setup() -> DatabasePostgres:
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

    return DatabasePostgres(db_config=db_config)
