def colored_print(text, color):
    if color == 'red':
        return '\033[91m{0}\033[0m'.format(text)
    elif color == 'green':
        return '\033[92m{0}\033[0m'.format(text)
    elif color == 'purple':
        return '\033[95m{0}\033[0m'.format(text)
    elif color == 'blue':
        return '\033[96m{0}\033[0m'.format(text)
    else:
        return '\033[30m{0}\033[0m'.format(text)


def in_board_range(board, position):
    return not (position[0] < 0 or position[0] > board.size - 1 or position[1] < 0 or position[1] > board.size - 1)


def are_adjacent(position1, position2):
    # Equivalent to say that the distance between the two positions is 1 -> Adjacent
    # Normally would square the differences and root the sum -> No need since only important values are 0, 1
    return (abs(position1[0] - position2[0])) + (abs(position1[1] - position2[1])) == 1


def get_column(board, index):
    return [board.candies[i][index] for i in range(board.size)]


def set_column(board, index, column):
    for i in range(board.size):
        board.candies[i][index] = column[i]


# Fonction obligatoire pour le projet
def test_detecte_coordonnees_combinaison(grille, i, j):
    print(grille.get_full_candies_chain((i, j)))
