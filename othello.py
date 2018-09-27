import os
import random
import sys

class Piece:
    def __init__(self, x, y, c):
        self.x, self.y, self.color = x, y, c

    def flip(self):
        if self.color == 'b':
            self.color = 'w'
        else:
            self.color = 'b'

class Board:
    def __init__(self):
        self.pieces = [Piece(4, 4, 'b'), Piece(5, 5, 'b'), Piece(4, 5, 'w'), Piece(5, 4, 'w')]

    def white_num(self):
        count = 0
        for i in self.pieces:
            if i.color == 'w':
                count += 1
        return count

    def black_num(self):
        count = 0
        for i in self.pieces:
            if i.color == 'b':
                count += 1
        return count

    def display(self):
        print("   Board")
        print("   +---+---+---+---+---+---+---+---+")
        for y in range(8, 0, -1):
            print(" " + str(y) + " | ", end = '')
            for x in range(1, 9, 1):
                if self.get_piece(x, y):
                    if self.get_piece(x, y).color == 'b':
                        print('b', end = '')
                    elif self.get_piece(x, y).color == 'w':
                        print('w', end = '')
                else:
                    print (' ', end = '')
                print(" | ", end = '')
            print("\n   +---+---+---+---+---+---+---+---+")
        print("     1   2   3   4   5   6   7   8  ")

    def get_piece(self, x, y):
        for i in self.pieces:
            if i.x == x and i.y == y:
                return i
        return False

    def get_color(self, x, y):
        for i in self.pieces:
            if i.x == x and i.y == y:
                return i.color
        return False

    def in_range(self, x, y):
        return x >= 1 and x <= 8 and y >= 1 and y <= 8

    def check_move(self, x, y, color): # returns list of legal flips
        if self.get_piece(x, y) or not self.in_range(x, y):
            return []

        tiles_to_flip = []
        if color == 'w':
            opp_color = 'b'
        else:
            opp_color = 'w'

        for xdir, ydir in [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]:
            xcurr, ycurr, count = x, y, 0
            xcurr += xdir
            ycurr += ydir
            while self.in_range(xcurr, ycurr) and self.get_color(xcurr, ycurr) == opp_color:
                xcurr += xdir
                ycurr += ydir
                count += 1
            if (self.get_color(xcurr, ycurr) == color and count > 0):
                xcurr -= xdir
                ycurr -= ydir
                while xcurr != x or ycurr != y:
                    tiles_to_flip.append([xcurr, ycurr])
                    xcurr -= xdir
                    ycurr -= ydir

        return tiles_to_flip

    def make_move(self, flips, x, y, color): # flips coordinates in flip list
        for i in flips:
            self.get_piece(i[0], i[1]).flip()
        self.pieces.append(Piece(x, y, color))

    def check_legal(self, color): # check_move for all coords of a color
        for x in range(1, 9, 1):
            for y in range(1, 9, 1):
                if self.check_move(x, y, color) != []:
                    return True
        return False

    def execute(self):
        os.system('cls')
        choice = int(input("Choose mode:\n(1)Free Play\n(2)Beginner AI\n(3)Intermediate AI\n"))

        x, y, numFlips, turn = 0, 0, 0, 1
        col = ["w","b"]

        while b.check_legal("w") or b.check_legal("b"):
            flips = []

            if turn % 2 == 1 or choice == 1:
                first = True
                while flips == []:
                    os.system('cls')
                    self.display()

                    if choice == 1 and col[turn % 2] == 'w':
                        print("White's turn\n")
                    elif choice == 1 and col[turn % 2] == 'b':
                        print("Black's turn\n")
                    else:
                        print("Your turn (black)\n")

                    if first and turn != 1 and choice != 1:
                        print("Computer placed a piece at (" + str(x) + ", " + str(y) + ") and flipped " + str(numFlips) + " pieces")
                    if flips == [] and first == False:
                        print("Illegal move\n")

                    x = int(input("X: "))
                    y = int(input("Y: "))
                    flips = b.check_move(x, y, col[turn % 2])
                    print(b.check_legal(col[turn % 2]))
                    first = False
                b.make_move(flips, x, y, col[turn % 2])
            elif choice == 2:
                x, y, numFlips = b.beginner_AI(turn)
            elif choice == 3:
                x, y, numFlips = b.intermediate_AI(turn)

            if b.check_legal(col[(turn + 1) % 2]):
                turn += 1

        os.system('cls')
        b.display()
        print("Game over")
        print("Black pieces: " + str(b.black_num()))
        print("White pieces: " + str(b.white_num()))

        if b.black_num() > b.white_num():
            print("Black wins")
        elif b.white_num() > b.black_num():
            print("White wins")
        else:
            print("Tie")

    def beginner_AI(self, turn):
        col = ['w', 'b']
        while True:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            flips = b.check_move(x, y, col[turn % 2])
            if flips != []:
                break
        b.make_move(flips, x, y, col[turn % 2])
        return [x, y, len(flips)]

    def intermediate_AI(self, turn): # + randint(0, 6) % 8 + 1
        col = ['w', 'b']
        flips = []
        range = [1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(range)
        for x in range:
            for y in range:
                if len(b.check_move(x, y, col[turn % 2])) > len(flips):
                    flips = b.check_move(x, y, col[turn % 2])
                    bestx = x
                    besty = y
        b.make_move(flips, bestx, besty, col[turn % 2])
        return [bestx, besty, len(flips)]


b = Board()
b.execute()
