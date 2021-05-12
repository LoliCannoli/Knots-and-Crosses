import random

class Board():

    def __init__(self):
        self.turn = 'X'
        self.nodes = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_'],
        ]
        self.unoccupied = [(colI, rowI) for colI, col in enumerate(self.nodes) for rowI, node in enumerate(col)]
        print(self.unoccupied)

    def place(self, x, y):
        self.nodes[y - 1][x - 1] = self.turn

        if(board.checkWin(self.turn)):
            print(self.turn + '\'s win')
            return

        self.unoccupied.pop(self.unoccupied.index((x, y)))

        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def printBoard(self):
        for row in self.nodes:
            for node in row:
                print(node, end = ' ')
            print()
        print()

    def checkWin(self, character):
        for x in range(3):
            if self.nodes[x][0] == self.nodes[x][1] == self.nodes[x][2] == character:
                return True
            if self.nodes[0][x] == self.nodes[1][x] == self.nodes[2][x] == character:
                return True
            if self.nodes[0][0] == self.nodes[1][1] == self.nodes[2][2] == character:
                return True
            if self.nodes[2][0] == self.nodes[1][1] == self.nodes[0][2] == character:
                return True
            return False

board = Board()

class Computer():

    def __init__(self, char):
        self.char = char


    def defense(self,):
        binaryTable = [[int(node == self.char) for node in row] for row in board.nodes ]
        print(binaryTable)

    def attack():
        pass

board.place(1,2)

comp = Computer('X')
comp.defense()



# board.place(1,1)
# computerTurn()
# board.place(2,1)
# computerTurn()
# board.place(3,1)
#
# board.printBoard()
