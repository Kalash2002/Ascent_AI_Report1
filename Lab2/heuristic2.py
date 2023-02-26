from Board import step,Astar

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
        sum = 0
        for i in range(7):
            for j in range(7):
                if(frontier[l].board[i][j]==1):
                    sum = sum + pow(2,max(abs(3-i),abs(3-j)))
        if(sum<maxi):
            maxi = sum
            ind = l
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