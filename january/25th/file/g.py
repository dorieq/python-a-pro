import os

if os.path.exists('c.txt'):
    os.remove('c.txt')
else:
    print('This file does not exist')