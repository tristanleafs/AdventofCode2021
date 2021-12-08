import copy
import re
#import numpy as np
import math

lines = []
with open("data6.txt") as f:
    line = f.readline()

fishes = [int(s) for s in line if s.isdigit()]
#fishes = np.array(fishes)
# addFish = 0
# for k in range(257):
#     print(k)
#     for i in range(addFish):
#         fishes = np.append(fishes, [8])

#     addFish = 0
#     for i in range(fishes.shape[0]):
#         if(fishes[i] == 0):
#             fishes[i] = 6
#             addFish+=1
#         else:
#             fishes[i] -= 1

amount = [0,0,0,0,0,0,0,0,0]
for fish in fishes:
    amount[fish] += 1

for i in range(256):


    temp = amount[0]
    amount[0] = amount[1]
    amount[1] = amount[2]
    amount[2] = amount[3]
    amount[3] = amount[4]
    amount[4] = amount[5]
    amount[5] = amount[6]
    amount[6] = temp
    amount[6] += amount[7]
    amount[7] = amount[8]
    amount[8] = temp

sum = 0
for i in amount:
    sum += i

print(sum)
 