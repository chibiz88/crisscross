from typing import List, Optional


class Cell:
    symbol: Optional[str]
    position: int

    def __init__(self, pos):
        self.position = pos
        self.symbol = None

    def change(self, symbol):
        self.symbol = symbol

    @property
    def is_used(self):
        return self.symbol is not None


class Board:
    cells: List[Cell]

    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]


class Player:
    symbol: str
    name: str
    player_type: str

    def __init__(self, name: str, symbol: str, player_type: str = ''):
        self.symbol = symbol
        self.name = name
        self.player_type = player_type


class Game:
    board: Board
    first_player: Player
    second_player: Player

    def setup(self):
        self.board = Board()
        self.first_player = Player('peta', 'x')
        self.second_player = Player('214', 'o')

    def game_process(self):
        ...

    def run(self):
        self.setup()
        self.game_process()