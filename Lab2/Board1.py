#   different type of hueristic:
#
#   1. Sum of the all the peg’s manhattan distance from the center.
#   2. Sum of 2 exponential of maximum between horizontal and vertical distances of the peg from the center.
#
#

class step:
    def __init__(self):
        self.father = None
        self.depth = 0
        self.board = None

    def set_father(self, board):
        self.father = board

    def print(self):
        for i in range(7):
            for j in range(7):
                print(self.board[i][j], end=" ")
            print()
        print()

    def set_board(self, ins):
        self.board = [[ins[i][j] for j in range(7)] for i in range(7)]

    def get_father(self):
        return self.father

    def get_board(self):
        return self.board

    def inFrontier(self):
        for i in range(len(frontier)):
            if frontier[i].board == self.board:
                return True
        return False

    def isVisited(self):

        for i in range(len(visited)):
            if visited[i].board == self.board:
                return True
        return False

    def setDepth(self, dep):
        self.depth = dep

    def final(self):
        return self.board == goal

    def peg_count(self):
        m = 0
        for i in range(7):
            for j in range(7):
                if self.board[i][j] == 1:
                    m += 1
        return m


class Astar(step):
    def heuristic1(self):
        sum = 0
        for i in range(7):
            for j in range(7):
                if self.board == 1:
                    sum += abs(i-3)+abs(j-3)
        return sum

    def Astarh1(self):
        return self.depth + self.heuristic1()

frontier = []
visited = []
intial_board = [
    [-1, -1, 1, 1, 1, -1, -1],
    [-1, -1, 1, 1, 1, -1, -1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [-1, -1, 1, 1, 1, -1, -1],
    [-1, -1, 1, 1, 1, -1, -1]
]
goal = [
    [-1, -1, 0, 0, 0, -1, -1],
    [-1, -1, 0, 0, 0, -1, -1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [-1, -1, 0, 0, 0, -1, -1],
    [-1, -1, 0, 0, 0, -1, -1],
]

start = Astar()
start.set_board(intial_board)
frontier.append(start)

while len(frontier):

    maxi = 4900
    ind = 0
    for l in range(len(frontier)):
        if frontier[l].depth <= maxi:
            maxi = frontier[l].depth
            ind = l
    # print(maxi)
    front = frontier.pop(ind)
    print(front.peg_count())
    if front.final():
        print("Peg Solitaire solved")
        front.print()
        break
    else:
        for i in range(7):
            for j in range(5):
                if front.board[i][j] == 1 and front.board[i][j+1] == 1 and front.board[i][j+2] == 0:
                    front1 = Astar()
                    front1.set_board(front.board)
                    front1.board[i][j] = 0
                    front1.board[i][j+1] = 0
                    front1.board[i][j+2] = 1
                    front1.setDepth(front.depth+1)
                    front1.set_father(front)
                    if front1.isVisited() == False and front1.inFrontier() == False:
                        # front1.print()
                        frontier.append(front1)
                if front.board[i][j] == 0 and front.board[i][j+1] == 1 and front.board[i][j+2] == 1:
                    front1 = Astar()
                    front1.set_board(front.board)
                    front1.board[i][j] = 1
                    front1.board[i][j+1] = 0
                    front1.board[i][j+2] = 0
                    front1.setDepth(front.depth+1)
                    front1.set_father(front)
                    if front1.isVisited() == False and front1.inFrontier() == False:
                        # front1.print()
                        frontier.append(front1)
        for i in range(5):
            for j in range(7):
                if front.board[i][j] == 1 and front.board[i+1][j] == 1 and front.board[i+2][j] == 0:
                    front1 = Astar()
                    front1.set_board(front.board)
                    front1.board[i][j] = 0
                    front1.board[i+1][j] = 0
                    front1.board[i+2][j] = 1
                    front1.setDepth(front.depth+1)
                    front1.set_father(front)
                    if front1.isVisited() == False and front1.inFrontier() == False:
                        # front1.print()
                        frontier.append(front1)
                if front.board[i][j] == 0 and front.board[i+1][j] == 1 and front.board[i+2][j] == 1:
                    front1 = Astar()
                    front1.set_board(front.board)
                    front1.board[i][j] = 1
                    front1.board[i+1][j] = 0
                    front1.board[i+2][j] = 0
                    front1.setDepth(front.depth+1)
                    front1.set_father(front)
                    if front1.isVisited() == False and front1.inFrontier() == False:
                        # front1.print()
                        frontier.append(front1)
        front.print()
        visited.append(front)