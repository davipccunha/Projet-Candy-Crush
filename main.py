import entities
import commons

BOARD_SIZE = 10
board = entities.Board(BOARD_SIZE)
board.start_game()
board.print_board()

# for i in range(BOARD_SIZE):
#     for j in range(BOARD_SIZE):
#         print(board.get_full_candies_chain((i, j)))

while True:
    x1, y1 = input('Enter first position: ').split()
    commons.in_board_range(board, (int(x1), int(y1)))
    x2, y2 = input('Enter second position: ').split()
    commons.in_board_range(board, (int(x2), int(y2)))

    if not (commons.in_board_range(board, (int(x1), int(y1))) and commons.in_board_range(board, (int(x2), int(y2)))):
        print('Position out of range\n')
        continue
    if not commons.are_adjacent((int(x1), int(y1)), (int(x2), int(y2))):
        print('Coordinates are not adjacent\n')
        continue

    board.swap_candies((int(x1), int(y1)), (int(x2), int(y2)))
    candy1_chain = board.get_full_candies_chain((int(x1), int(y1)))
    candy2_chain = board.get_full_candies_chain((int(x2), int(y2)))

    print()

    if len(candy1_chain) >= 3:
        board.pop_candies(candy1_chain)
        board.drop_columns([position[1]
                           for position in list(dict.fromkeys(candy1_chain))])
    if len(candy2_chain) >= 3:
        board.pop_candies(candy2_chain)
        board.drop_columns([position[1]
                            for position in list(dict.fromkeys(candy2_chain))])

    board.print_board()
