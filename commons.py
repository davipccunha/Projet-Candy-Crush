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
        return '\033[0m{0}'.format(text)
    

def input_in_board_range(board, position):
    if position[0] < 0 or position[0] > board.size - 1 or position[1] < 0 or position[1] > board.size - 1:
        return False
    return True


def are_adjacent(position1, position2):
    if position1 == position2:
        return False
    if abs(position1[0] - position2[0]) > 1 or abs(position1[1] - position2[1]) > 1:
        return False
    return True