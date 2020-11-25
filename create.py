import argparse

from src.minesweeper_api import MinesweeperApi

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--height', help='Number of rows')
    parser.add_argument(
        '--width', help="Number of columns"
    )
    parser.add_argument(
        '--mines', help='Number of mines to include in board'
    )

    args = parser.parse_args()

    response = MinesweeperApi().create({
        "height": args.height,
        "width": args.width,
        "mines": args.mines,
    })

    print(f'Status code: {response.status_code}')
    print(response.json())
