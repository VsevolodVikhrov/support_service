from os import getenv
from dotenv import load_dotenv

load_dotenv()
NAME = getenv('NAME')
DBUSER = getenv('DBUSER')
PASSWORD = getenv('PASSWORD')
DJANGO_SECRET_KEY = getenv('DJANGO_SECRET_KEY')

DEBUG = getenv("DEBUG", 'False') in 'True'

