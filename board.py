from pieces import Piece

# class used to set up the grid and position pieces
class Board:
    def __init__(self):
        # creates 8x8 2d list, filled with 'None'
        self.grid = [ [None] * 8 for _ in range(8) ]
        # calls method below
        self.setup_pieces()

    # used to place pieces in the grid created
    def setup_pieces(self):
        # list which will be used for back row to fill grid
        back_row = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

        # black pieces rows 0 and 1
        # loops back row list, enumerate gives both index and value of each element
        for col, piece_type in enumerate(back_row):
            # fills grid at row zero for each column with Piece objects
            self.grid[0][col] = Piece('black', piece_type, 0, col)
            # fills second row with pawns
            self.grid[1][col] = Piece('black', 'pawn', 1, col)

        # white pieces rows 6 and 7
        for col, piece_type in enumerate(back_row):
            self.grid[7][col] = Piece('white', piece_type, 7, col)
            self.grid[6][col] = Piece('white', 'pawn', 6, col)

# Board class ends here