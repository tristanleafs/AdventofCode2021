from collections import deque
def checkBottom(grid, row, col):
    value = grid[row][col]
    if(value < grid[row+1][col]
        and value < grid[row-1][col]
        and value < grid[row][col+1]
        and value < grid[row][col-1]):
        return True
    else:
        return False

def solveMaze(maze, start):
    R, C = len(maze), len(maze[0])

    size = 0

    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]

    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True
        size += coord[2]
        

        for dir in directions:
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] >= 9 or visited[nr][nc]): continue
            queue.appendleft((nr, nc, 1))
            visited[nr][nc] = True
    return size +1

grid = []
lines = []
with open("data9.txt") as f:
    lines = f.readlines()

grid.append([10]*105)

for index , line in enumerate(lines):
    grid.append([])
    grid[index+1].append(10)
    for char in line:
        if(char != '\n'):
            grid[index+1].append(int(char))
    grid[index+1].append(10)
grid.append([10]*105)
#go threough grid


sum = 0
for row in range(1, len(grid)-1):
    for col in range(1, len(grid[row])-1):
        value = grid[row][col]
        if(value < grid[row+1][col]
        and value < grid[row-1][col]
        and value < grid[row][col+1]
        and value < grid[row][col-1]):
            #print(value, row, col)
            sum += 1 + value

print("part 1 ans:", sum)

#part 2
sizes = []


for row in range(1, len(grid)-1):
    for col in range(1, len(grid[row])-1):
        if(checkBottom(grid, row, col)):
            sizes.append(solveMaze(grid, (row, col)))

sizes.sort(reverse=True)
ans = 1
for i in range(3):
    ans *= sizes[i]

print("part 2 ans:", ans)