import pygame
from pieces import Piece
from constans import LIGHT_SQUARE,  DARK_SQUARE, SQUARE_SIZE

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

    # screen is the parameter used for pygame window surface
    def draw(self, screen):
        # list holding color values, so index can be used
        colors = [LIGHT_SQUARE, DARK_SQUARE]
        # 2d loop to go through each square
        for row in range(8):
            for col in range(8):
                # returns either 0 or 1 depending on sum of row and col being odd or even
                # index used to create pattern
                color = colors[ (row + col) % 2 ]
                # draws, ( x, y, width, height)
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # drawing pieces (placeholder for now)
    def draw_pieces(self, screen, font):
        # loop to visit every square
        for row in range(8):
            for col in range(8):
                # grabs element in grid
                piece = self.grid[row][col]
                # only runs if element is not "None"
                if piece is not None:
                    # calculates coordinates within a square
                    center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                    # picks color
                    color = (255, 255, 255) if piece.color == 'white' else (30, 30, 30)
                    # draws circle acting as a piece
                    pygame.draw.circle(screen, color, center, SQUARE_SIZE // 2 - 8)
                    # grabs first letter for id, BUG: knight and king start with k, fix after
                    letter = piece.piece_type[0].upper()
                    # creates letter to id piece
                    text = font.render(letter, True, (255, 0, 0))
                    # blit -> draws letter on top of another surface
                    screen.blit(text, text.get_rect(center=center))




















































# Board class ends here