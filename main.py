import entities
import commons

board = entities.Board(5)
board.start_game()
board.print_board()

while True:
    x1, y1 = input('Enter first position: ').split()
    commons.input_in_board_range(board, (int(x1), int(y1)))
    x2, y2 = input('Enter second position: ').split()
    commons.input_in_board_range(board, (int(x2), int(y2)))

    if not (commons.input_in_board_range(board, (int(x1), int(y1))) and commons.input_in_board_range(board, (int(x2), int(y2)))): 
        print('Invalid positions')
        continue
    if not commons.are_adjacent((int(x1), int(y1)), (int(x2), int(y2))):
        print('Coordinates are not adjacent')
        continue

    board.swap_candies((int(x1), int(y1)), (int(x2), int(y2)))
    board.print_board()