import sys
from modules import Fetcher

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <usuario>")
        sys.exit(1)
    
    username = sys.argv[1]
    fetcher = Fetcher(username)
    fetcher.fetch()