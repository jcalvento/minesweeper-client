import argparse

from src.minesweeper_api import MinesweeperApi

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', help='Id of the game you want to resume')
    parser.add_argument(
        '--url', help='Optional arg if you want to use a custom API url'
    )
    args = parser.parse_args()

    response = MinesweeperApi(args.url).show(args.id)

    print(f'Status code: {response.status_code}')
    print(response.json())
