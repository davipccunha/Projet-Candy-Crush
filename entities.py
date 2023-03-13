import random
import commons

COLORS = ['red', 'blue', 'green', 'purple']

class Candy:
    def __init__(self, color, position):
        self.color = color
        self.position = position


class Board:
    def __init__(self, size):
        self.size = size
        self.candies = [[None for _ in range(size)] for _ in range(size)]

    def start_game(self):
        self.candies = [[Candy(random.choice(COLORS), (i, j)) for j in range(self.size)] for i in range(self.size)]

    def print_board(self):
        for row in self.candies:
            for candy in row:
                print(commons.colored_print('o', candy.color), end=' ')
            print()

    def get_candy(self, position):
        return self.candies[position[0]][position[1]]
    
    def swap_candies(self, position1, position2):
        candy1 = self.get_candy(position1)
        candy2 = self.get_candy(position2)
        self.candies[position1[0]][position1[1]] = candy2
        self.candies[position2[0]][position2[1]] = candy1
        candy1.position = position2
        candy2.position = position1
    
