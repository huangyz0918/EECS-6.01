# Mazes
from lib601.search import search

# set up lists of strings to represent the four test mazes
smallMazeText = [line.strip() for line in open('smallMaze.txt').readlines()]
mediumMazeText = [line.strip() for line in open('mediumMaze.txt').readlines()]
largeMazeText = [line.strip() for line in open('largeMaze.txt').readlines()]
hugeMazeText = [line.strip() for line in open('hugeMaze.txt').readlines()]

class Maze:
    def __init__(self, mazeText):
        self.width = len(mazeText[0])
        self.height = len(mazeText)
        self.mazeText = mazeText
        # Start Row/Column Variables
        row_count = 0
        column_count = 0

        # Start Row
        for row in mazeText:
            if 'S' in row:
                start_row = row_count
            else:
                row_count += 1

        # Start Column
        for column in mazeText[start_row]:
            if column == 'S':
                start_column = column_count
            else:
                column_count += 1
        self.start = (start_row, start_column)
        
        
        # End Row/Column Variables
        row_count = 0
        column_count = 0

        # End Row
        for row in mazeText:
            if 'G' in row:
                end_row = row_count
            else:
                row_count += 1

        # End Column
        for column in mazeText[end_row]:
            if column == 'G':
                end_column = column_count
            else:
                column_count += 1
        self.goal = (end_row, end_column)
        

    def isPassable(self, (r,c)):
        # Input out of Maze Range
        if r >= self.width or c >= self.height or r < 0 or c < 0:
            return False
        else:
            # Input at row and column if '#' False
            if self.mazeText[r][c] == '#':
                return False
            else:
                return True

def maze_successors(maze):
    def nextsteps(point):
        possible_moves = []
        r,c = point
        if maze.isPassable((r+1,c)):
            possible_moves.append((r+1,c))
        if maze.isPassable((r,c+1)):
            possible_moves.append((r,c+1))
        if maze.isPassable((r-1,c)):
            possible_moves.append((r-1,c))
        if maze.isPassable((r,c-1)):
            possible_moves.append((r,c-1))
        return possible_moves
    return nextsteps


def mazetest():
    m = Maze(largeMazeText)
    ans = [m.width,m.height,m.start,m.goal]
    print m
    print ans

def mazetest1():
    m = Maze(smallMazeText)
    ans = [((r,c), m.isPassable((r,c))) for r in xrange(1,4) for c in xrange(2,4)]
    print m
    print ans

def mazetest2():
    m = Maze(smallMazeText)
    ans = [((r,c), m.isPassable((r,c))) for r in xrange(-1,1) for c in xrange(7,10)]
    print m
    print ans

def mstest():
    m = Maze(mediumMazeText)
    c = maze_successors(m)(m.start)
    ans = list(sorted(c))
    print ans

small = Maze(hugeMazeText)
goaltest = lambda (r,c): (r,c) == small.goal

print len(search(maze_successors(small), small.start, goaltest, dfs=False))

