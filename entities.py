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
        self.candies = [[Candy(random.choice(COLORS), (i, j))
                         for j in range(self.size)] for i in range(self.size)]

    def print_board(self):
        for row in self.candies:
            for candy in row:
                print(commons.colored_print(
                    'o', candy.color if candy is not None else ''), end=' ')
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

    # detecte_coordonnees_combinaison(grille, i, j) écrite différemment
    def get_full_candies_chain(self, position):
        candy_type = self.get_candy(position).color
        candies_chain = [self.get_candy(position)]
        candies_to_check = [self.get_candy(position)]

        while len(candies_to_check) > 0:
            candy = candies_to_check.pop()

            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_position = (
                    candy.position[0] + direction[0], candy.position[1] + direction[1])

                if commons.in_board_range(self, next_position):
                    next_candy = self.get_candy(next_position)

                    if next_candy.color == candy_type and next_candy not in candies_chain:
                        candies_chain.append(next_candy)
                        candies_to_check.append(next_candy)

        return [candy.position for candy in candies_chain]

    def pop_candies(self, candies_chain):
        for position in candies_chain:
            self.candies[position[0]][position[1]] = None

    def drop_columns(self, columns_indexes):
        for index in columns_indexes:
            column = commons.get_column(self, index)
            column.sort(key=lambda candy: candy is not None)
            commons.set_column(self, index, column)

    def regenerate_candies(self):
        regenerated_candies = []

        for i, row in enumerate(self.candies):
            for j, candy in enumerate(row):
                if candy is None:
                    new_candy = Candy(random.choice(COLORS), (i, j))
                    self.candies[i][j] = new_candy
                    regenerated_candies.append(new_candy)

        return regenerated_candies
    
    
