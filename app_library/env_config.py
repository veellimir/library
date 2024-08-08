import os

from dotenv import load_dotenv

load_dotenv()

PROJECT_SECRET_KEY = os.getenv("PROJECT_SECRET_KEY")
PROJECT_DEBUG = os.getenv("PROJECT_DEBUG")
PROJECT_DOMAIN_NAME = os.getenv("PROJECT_DOMAIN_NAME")

