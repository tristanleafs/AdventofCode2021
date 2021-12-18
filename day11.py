import numpy as np

lines = []
with open("data11.txt") as f:
    lines = f.readlines()

powers = []
for i, line in enumerate(lines):
    powers.append([])
    for char in line:
        if(char != '\n'):
            powers[i].append(int(char))


powers = np.array(powers)
powers = np.pad(powers, [(1, 1), (1, 1)], mode='constant', constant_values=12)

#steps
flashes = 0
step = 0
for i in range(300):
    rows,cols = powers.shape
    visited = [[False] * rows for _ in range(cols)]
    #for fuck in range(5):
    
    for row in range(rows):
            for col in range(cols):
                if(powers[row][col] < 10):
                                powers[row][col] += 1

    for fuck in range(15):
        

        for row in range(rows):
            for col in range(cols):
                
                if(powers[row][col] == 10 and not visited[row][col]):
                    visited[row][col] = True
                    for k in range(-1, 2):
                        for h in range(-1, 2):
                            if(powers[row+k][col+h] < 10):
                                powers[row+k][col+h] += 1

    temp = flashes
    for row in range(rows):
            for col in range(cols):
                if(powers[row][col] == 10):
                    flashes += 1
                    powers[row][col] = 0
    if(flashes - temp == 100):
        step = i+1
        break

print(powers)
print("part 1 ans:",flashes)
print("part 2 ans:" ,step)