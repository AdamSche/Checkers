import pygame

# Initialize pygame
pygame.init()

# Define constants
WINDOW_SIZE = 800
NUM_SQUARES = 8
SQUARE_SIZE = WINDOW_SIZE // NUM_SQUARES

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Create the game window
display = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Checkers")

# Define the main function
def main():
    # Initialize the game board
    global selected_pawn
    selected_pawn = None
    checkerboard = [[0, 1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 2, 0, 2, 0, 2, 0],
                    [0, 2, 0, 2, 0, 2, 0, 2],
                    [2, 0, 2, 0, 2, 0, 2, 0]]

    # Create a font object
    font = pygame.font.SysFont(None, 48)

    # Set the initial player turn
    player_turn = 1

    # Define a function to get the board coordinates of a given pixel coordinate
    def get_coord(x, y):
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    # Run the game loop
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Check for a mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            x, y = pygame.mouse.get_pos()
            row, col = get_coord(x, y)

            # Check if the selected square contains a pawn belonging to the current player
            if checkerboard[row][col] == player_turn:
                # Check if the user has already selected a pawn to move
                if selected_pawn is None:
                    selected_pawn = (row, col)
                else:
                    # If the user has already selected a pawn, try to move it to the selected square
                    dest_row, dest_col = selected_pawn
                    move_successful = make_move(checkerboard, player_turn, dest_row, dest_col, row, col)




