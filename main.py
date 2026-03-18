import pygame
from constans import WINDOW_SIZE
from board import Board

# ***** MAIN FUNCTION *****
def main():
    pygame.init() # starts up all pygame subsystems
    # creates window and returns "surface" to draw into
    screen = pygame.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
    pygame.display.set_caption("Chess") # title bar
    clock = pygame.time.Clock() # clock object to control how fast loop runs

    # board object
    board = Board()

    # game loop
    running = True
    while running:
        # checks for an event each frame
        for event in pygame.event.get():
            # sets game loop to false when "x" is clicked
            if event.type == pygame.QUIT:
                running = False

        # paints window black, done each frame before drawing again
        screen.fill((0, 0, 0))
        # calls draw function from Board class
        board.draw(screen)

        # drawing done off-screen and then made visible, prevents flickering
        pygame.display.flip()
        # runs game loop at a maximum of 60 fps
        clock.tick(60)

    pygame.quit() # shuts down pygame cleanly after loop ends
# main() ends here

# convention, only run main() if this file is being run directly
if __name__ == "__main__":
    main()

