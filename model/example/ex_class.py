import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
HOME_DIR = os.getenv("CLASSES_DIR")

sys.path.append(HOME_DIR)

class Ex_Class(object):

    def __init__(self, print_msg='Hello World'):
        self.msg = print_msg
    
    def __str__(self):
        print(self.msg)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Ex_Class())

if __name__ == '__main__':
    main()