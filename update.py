import argparse

from src.minesweeper_api import MinesweeperApi

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', help='Id of the game you want to update')
    parser.add_argument('--x', help='X position of the coordinate in the board')
    parser.add_argument(
        '--y', help="Y position of the coordinate in the board"
    )
    parser.add_argument(
        '--command', help="Command for the given cell. Could be 'red_flag', 'delete_flag', 'question_mark' or 'uncover'"
    )
    parser.add_argument(
        '--url', help='Optional arg if you want to use a custom API url'
    )

    args = parser.parse_args()

    response = MinesweeperApi(args.url).update(args.id, {
        "x": args.x,
        "y": args.y,
        "command": args.command,
    })

    print(f'Status code: {response.status_code}')
    print(response.json())
