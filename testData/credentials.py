import os

from dotenv import load_dotenv

load_dotenv('.env')

TEST_USER = {
    'email': os.getenv('TEST_USER_EMAIL'),
    'password': os.getenv('TEST_USER_PASSWORD')
}
