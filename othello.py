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

    def whiteNum(self):
        count = 0
        for i in self.pieces:
            if i.color == 'w':
                count += 1
        return count

    def blackNum(self):
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
                if self.getPiece(x, y):
                    if self.getPiece(x, y).color == 'b':
                        print('b', end = '')
                    elif self.getPiece(x, y).color == 'w':
                        print('w', end = '')
                else:
                    print (' ', end = '')
                print(" | ", end = '')
            print("\n   +---+---+---+---+---+---+---+---+")
        print("     1   2   3   4   5   6   7   8  ")

    def getPiece(self, x, y):
        for i in self.pieces:
            if i.x == x and i.y == y:
                return i
        return False

    def getColor(self, x, y):
        for i in self.pieces:
            if i.x == x and i.y == y:
                return i.color
        return False

    def inRange(self, x, y):
        return x >= 1 and x <= 8 and y >= 1 and y <= 8

    def checkMove(self, x, y, color): # returns list of legal flips
        if self.getPiece(x, y) or not self.inRange(x, y):
            return []

        tilesToFlip = []
        if color == 'w':
            oppColor = 'b'
        else:
            oppColor = 'w'

        for xdir, ydir in [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]:
            xcurr, ycurr, count = x, y, 0
            xcurr += xdir
            ycurr += ydir
            while self.inRange(xcurr, ycurr) and self.getColor(xcurr, ycurr) == oppColor:
                xcurr += xdir
                ycurr += ydir
                count += 1
            if (self.getColor(xcurr, ycurr) == color and count > 0):
                xcurr -= xdir
                ycurr -= ydir
                while xcurr != x or ycurr != y:
                    tilesToFlip.append([xcurr, ycurr])
                    xcurr -= xdir
                    ycurr -= ydir

        return tilesToFlip

    def makeMove(self, flips, x, y, color): # flips coordinates in flip list
        for i in flips:
            self.getPiece(i[0], i[1]).flip()
        self.pieces.append(Piece(x, y, color))

    def checkLegal(self, color): # checkMove for all coords of a color
        for x in range(1, 9, 1):
            for y in range(1, 9, 1):
                if self.checkMove(x, y, color) != []:
                    return True
        return False

    def execute(self):
        os.system('cls')
        choice = int(input("Choose mode:\n(1)Free Play\n(2)Beginner AI\n(3)Intermediate AI\n"))

        x, y, numFlips, turn = 0, 0, 0, 1
        col = ["w","b"]

        while b.checkLegal("w") or b.checkLegal("b"):
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
                    flips = b.checkMove(x, y, col[turn % 2])
                    print(b.checkLegal(col[turn % 2]))
                    first = False
                b.makeMove(flips, x, y, col[turn % 2])
            elif choice == 2:
                x, y, numFlips = b.beginnerAI(turn)
            elif choice == 3:
                x, y, numFlips = b.intermediateAI(turn)

            if b.checkLegal(col[(turn + 1) % 2]):
                turn += 1

        os.system('cls')
        b.display()
        print("Game over")
        print("Black pieces: " + str(b.blackNum()))
        print("White pieces: " + str(b.whiteNum()))

        if b.blackNum() > b.whiteNum():
            print("Black wins")
        elif b.whiteNum() > b.blackNum():
            print("White wins")
        else:
            print("Tie")

    def beginnerAI(self, turn):
        col = ['w', 'b']
        while True:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            flips = b.checkMove(x, y, col[turn % 2])
            if flips != []:
                break
        b.makeMove(flips, x, y, col[turn % 2])
        return [x, y, len(flips)]

    def intermediateAI(self, turn): # + randint(0, 6) % 8 + 1
        col = ['w', 'b']
        flips = []
        range = [1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(range)
        for x in range:
            for y in range:
                if len(b.checkMove(x, y, col[turn % 2])) > len(flips):
                    flips = b.checkMove(x, y, col[turn % 2])
                    bestx = x
                    besty = y
        b.makeMove(flips, bestx, besty, col[turn % 2])
        return [bestx, besty, len(flips)]


b = Board()
b.execute()
