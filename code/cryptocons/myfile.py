import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print('This is our base dir', BASE_DIR)

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
print('This is our site root', SITE_ROOT)
