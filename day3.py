lines = []
with open("data3.txt") as f:
    lines = f.readlines()


frequency1 = [[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0]]

frequency2 = [[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0]]


lineLen = len(lines[0])
gammaLay = ""
epLay = ""
oxygen = ""
co2 = ""

for i in range(lineLen-1):
    count1 = 0
    count2 = 0
    for line in lines:
            if(line.startswith(gammaLay)):
                count1+=1
                if(int(line[i])): frequency1[0][i] += 1
                else: frequency1[1][i] += 1
            if(line.startswith(epLay)):
                count2 +=1
                if(int(line[i])): frequency2[0][i] += 1
                else: frequency2[1][i] += 1

    if(count1 == 1):
        for line in lines:
            if(line.startswith(gammaLay)):
                oxygen = line
    if(count2 == 1):
        for line in lines:
            if(line.startswith(epLay)):
                co2 = line


    if(frequency1[0][i] >= frequency1[1][i]):
        gammaLay = gammaLay + "1"
    else:
        gammaLay = gammaLay + "0"
    if(frequency2[0][i] >= frequency2[1][i]):
        epLay = epLay + "0"
    else:
        epLay = epLay + "1"
    
        
    print("count1", count1)
    print("count2", count2)
    

if(len(oxygen) < 1):
    oxygen = gammaLay
if(len(co2) < 1):
    co2 = epLay




gamma = 0
ep = 0
# for i in range(12):
#     if(frequency[0][i] > frequency[1][i]): gamma += 2**(4-i)
#     else: ep += 2**(11-i)

for i in range(len(oxygen)):
    gamma += 2**(11-i)*int(oxygen[i])
    ep += 2**(11-i)*int(co2[i])

print(frequency1)
print (frequency2)
print(gammaLay)
print(epLay)
print("gamma", gamma)
print("epsilon", ep)
print("ans", gamma*ep)