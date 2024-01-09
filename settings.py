import os

from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
HOST_USER = os.getenv("HOST_USER")
HOST_PASSWORD = os.getenv("HOST_PASSWORD")