import os
from dotenv import load_dotenv
from supabase_py import create_client, Client
import psycopg2

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

host = os.getenv("SUPABASE_HOST")
db = os.getenv("SUPABASE_DB")
user = os.getenv("SUPABASE_USER")
port = os.getenv("SUPABASE_PORT")
passwd = os.getenv("SUPABASE_PASSWD")


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS BDAYS (
            id SERIAL PRIMARY KEY NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            name TEXT NOT NULL,
            bday DATE NOT NULL
        )
        """,
    )

    conn = None
    try:
        params = {
            'database': db,
            'user': user,
            'password': passwd,
            'host': host,
            'port': port
        }
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
# TODO
# def check_tables():

create_tables()
supabase: Client = create_client(url, key)
