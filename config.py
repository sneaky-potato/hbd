import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

host = os.getenv("SUPABASE_HOST")
database = os.getenv("SUPABASE_DB")
user = os.getenv("SUPABASE_USER")
port = os.getenv("SUPABASE_PORT")
passwd = os.getenv("SUPABASE_PASSWD")

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=user,pw=passwd,url=host + ':' + port,db=database)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = DB_URL 
FLASK_DEBUG = True