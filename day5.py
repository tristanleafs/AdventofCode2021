import copy
import re
import numpy as np
import math

lines = []
with open("data5.txt") as f:
    lines = f.readlines()

grid = np.zeros((1000,1000))


for line in lines:
    coo = [int(s) for s in re.split('; |,|\*|\n| ',line) if s.isdigit() ]
    y1 = coo[0]
    x1 = coo[1]
    y2 = coo[2]
    x2 = coo[3]

    rate = 1
    if(y1 == y2):
        if(x1 > x2): 
            for i in range(x2, x1+1):
                grid[y1][i] += 1
        else:
            for i in range(x1, x2+1):
                grid[y1][i] += 1
                #print(grid[y1][i])
    elif(x1 == x2):
        if(y1 > y2):
            for i in range(y2, y1+1):
                grid[i][x1] += 1
        else:
            for i in range(y1, y2+1):
                grid[i][x1] += 1
                #print(grid[i][x1])
    #diagonal
    else:
        if(x1 > x2 and y1 > y2):
            for i in range(x1-x2+1):
                grid[y2+i][x2+i]+=1

        elif(x1 < x2 and y1 < y2):
            for i in range(x2-x1+1):
                grid[y1+i][x1+i]+=1
        #maybe broken
        elif(x1 > x2 and y1 < y2):
            for i in range(x1-x2+1):
                grid[y1+i][x1-i]+=1
        elif(x1 < x2 and y1 > y2):
            for i in range(x2-x1+1):
                grid[y2+i][x2-i]+=1
        

overlap = 0
for num in grid[grid>1]:
        overlap += 1


print(overlap)


