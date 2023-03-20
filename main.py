import entities
import commons

BOARD_SIZE = 5
board = entities.Board(BOARD_SIZE)
board.start_game()
board.print_board()

# for i in range(BOARD_SIZE):
#     for j in range(BOARD_SIZE):
#         print(board.get_full_candies_chain((i, j)))

while True:
    x1, y1 = input('Enter first position: ').split()
    x1 = int(x1) - 1
    y1 = int(y1) - 1

    commons.in_board_range(board, (x1, y1))
    x2, y2 = input('Enter second position: ').split()
    x2 = int(x2) - 1
    y2 = int(y2) - 1
    commons.in_board_range(board, (x2, y2))

    if not (commons.in_board_range(board, (x1, y1)) and commons.in_board_range(board, (x2, y2))):
        print('Position out of range\n')
        continue
    if not commons.are_adjacent((x1, y1), (x2, y2)):
        print('Coordinates are not adjacent\n')
        continue

    board.swap_candies((x1, y1), (x2, y2))
    candy1_chain = board.get_full_candies_chain((x1, y1))
    candy2_chain = board.get_full_candies_chain((x2, y2))

    print()

    if len(candy1_chain) >= 3:
        board.pop_candies(candy1_chain)
        board.drop_columns([position[1]
                           for position in list(dict.fromkeys(candy1_chain))])
        new_candies = board.regenerate_candies()

    if len(candy2_chain) >= 3:
        board.pop_candies(candy2_chain)
        board.drop_columns([position[1]
                            for position in list(dict.fromkeys(candy2_chain))])
        board.regenerate_candies()

    board.print_board()
