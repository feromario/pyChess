class Piece:
    # initializing object
    def __init__(self, color, piece_type, row, col):
        self.color        = color
        self.piece_type   = piece_type
        self.row          = row
        self.col          = col

    # string representation function
    def __repr__(self):
        return f"{self.color} {self.piece_type} at ({self.row}, {self.col})"

# Piece class ends here