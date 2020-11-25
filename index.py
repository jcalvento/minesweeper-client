from src.minesweeper_api import MinesweeperApi

if __name__ == "__main__":
    response = MinesweeperApi().index()

    print(f'Status code: {response.status_code}')
    print(response.json())
