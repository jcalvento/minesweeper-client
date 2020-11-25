import argparse

from src.minesweeper_api import MinesweeperApi

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', help='Id of the game you want to resume')

    args = parser.parse_args()

    response = MinesweeperApi().show(args.id)

    print(f'Status code: {response.status_code}')
    print(response.json())
