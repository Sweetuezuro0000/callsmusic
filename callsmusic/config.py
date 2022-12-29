from os import getenv

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'BQE4TGkAcIEEc6Ry6zv9yc0vHXJwhlmEFhMsQCSuHDJQB8cuF-kCG6XdbKFH8VlgBDwMQOUkuvXRmsgZ8sL6tsvpJIDj-KBOVkTnzOkaRWHam097C15riUWpUphlrFL4M73xPlC4R1yW08g6hYgPzplaKxEuVwowa7eNFsz5cHF1og54AeUhvW_9ZBqz_EzgfSi-Sj-NCNcRy45CpJbZGvfTu76Gd42j4YyvmIKKCY-9nJnvOX4fmkC4JSd_syU0wdHSFiYnZZ3SVZDL_FF4DxWHEVqt7ng86prmOXdLw-xaV8CoIDlFjcmkhn3J5raHX82mTNTSwvxK1K42gkUzp8BV7rJzTgAAAAFLXKjeAA')
BOT_TOKEN = getenv('BOT_TOKEN', '5816085578:AAFTwQXqq9Z-ULeZ0CstCMqU87Jul5hqaoE')
API_ID = int(getenv('API_ID', '20466793')
API_HASH = getenv('API_HASH', '5229101f02e28e6444d1e099013e0c69')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '10'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '5267531505 5559331038').split()))
