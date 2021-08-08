from os import getenv
from dotenv import load_dotenv

load_dotenv()

STRING = getenv("STRING")
STRING2 = getenv("STRING2")
STRING3 = getenv("STRING3")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BIO_MESSAGE = getenv("BIO")
ALIVE_NAME = getenv("ALIVE_NAME")
USERNAME = getenv("USERNAME")
SUDO = list(map(int, getenv("SUDO").split()))
