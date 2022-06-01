# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Board:
    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def change_sign(self, sign):
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"

    def place_symbol(self, case, person):
        self.state[case] = person.symbol

    def is_full(self):
        for i in self.state:
            if i == 0:
                return False
        return True

    def valid_turn(self, case):

        if self.state[case] == 0:
            return True
        return False

    def win_situation(self, case, person):
        s = person.symbol
        if self.state[0] == s and self.state[1] == s and self.state[2] == s:
            return True
        if self.state[3] == s and self.state[4] == s and self.state[5] == s:
            return True
        if self.state[6] == s and self.state[7] == s and self.state[3] == s:
            return True
        if self.state[0] == s and self.state[3] == s and self.state[6] == s:
            return True
        if self.state[1] == s and self.state[4] == s and self.state[7] == s:
            return True
        if self.state[2] == s and self.state[5] == s and self.state[8] == s:
            return True
        if self.state[0] == s and self.state[4] == s and self.state[8] == s:
            return True
        if self.state[2] == s and self.state[4] == s and self.state[6] == s:
            return True

    def print_board(self):

        print(" " + self.change_sign(self.state[0]) + " | " + "" + self.change_sign(
            self.state[1]) + " | " + "" + self.change_sign(self.state[2]) + "\n"
                                                                            " " + self.change_sign(
            self.state[3]) + " | " + "" + self.change_sign(self.state[4]) + " | " + "" + self.change_sign(
            self.state[5]) + "\n"
                             " " + self.change_sign(self.state[6]) + " | " + "" + self.change_sign(
            self.state[7]) + " | " + "" + self.change_sign(self.state[8]))


class Person:
    def __init__(self, symbol):
        self.symbol = symbol


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    player_a = Person(1)
    player_b = Person(-1)

    active_player = player_a
    cell = 0

    while not board.is_full():
        move_status = True
        board.print_board()

        print("\n --> It is your turn, Player " + "(" + board.change_sign(active_player.symbol) + "),")
        cell = int(input(" where do you want to place your sign? [1-9]: "))
        cell = cell - 1

        if cell < 0 or cell > 8:
            print("--> Please choose a value between 1 and 9!")
            continue
        else:
            if board.valid_turn(cell):
                board.place_symbol(cell, active_player)
            else:
                print("\n--> Invalid move! try again !")
                move_status = False
                continue

        if board.win_situation(cell, active_player):
            print("\n--> The player with the mark " + "(" + board.change_sign(active_player.symbol) + ")" + ' wins the game '
                                                                                                       '!')
            board.print_board()
            break

        if move_status:
            if active_player == player_a:
                active_player = player_b
            else:
                active_player = player_a
        continue

    if not board.win_situation(cell, active_player):
        print("\nIt is a draw !")
        board.print_board()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
