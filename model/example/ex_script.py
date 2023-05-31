import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
HOME_DIR = os.getenv("CLASSES_DIR")

sys.path.append(HOME_DIR)

from example.ex_class import Ex_Class

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Ex_Class())

if __name__ == '__main__':
    main()