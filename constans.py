import pygame

# ***** Board dimensions *****
BOARD_SIZE       = 8
SQUARE_SIZE      = 80
WINDOW_SIZE      = BOARD_SIZE * SQUARE_SIZE # 640px

# ***** Colors in RGB *****
LIGHT_SQUARE     = (240, 217, 181)
DARK_SQUARE      = (181, 136,  99)
HIGHLIGHT        = ( 20,  85,  30, 128)
SELECTED         = (255, 255,   0, 128)
TEXT_COLOR       = (255, 255, 255)

# ***** Piece id's used as dictionary keys *****
WHITE            = "white"
BLACK            = "black"
PIECE_TYPES      = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']