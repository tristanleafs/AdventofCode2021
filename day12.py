import copy
class cave:

    def __init__(self, id):
        self.id = id
        self.connects = []
    
    def add(self, otherCave):
        self.connects.append(otherCave)
        otherCave.connects.append(self)



def search(maze):
    start = maze["start"]

    moving = True
    moves = [[start.id]]
    finalMoves = []
    
    for count in range(15):
        print(count, len(moves))
        newMoves = []
        for move in moves:
            for jk in maze[move[-1]].connects:
                i = jk.id
                #print(i)
                
                if(i == "end"):
                    temp = copy.deepcopy(move)
                    temp.append(i)
                    
                    finalMoves.append(temp)
                else:    
                    temp = copy.deepcopy(move)
                    if(i == "start"):
                        pass
                    elif(i.islower()):
                        if(i not in temp):

                            temp.append(i)
                            
                            newMoves.append(temp)
                        elif("USED" in temp):
                            pass
                        else:
                            temp.append("USED")
                            temp.append(i)
                            
                            newMoves.append(temp)
                    
                    else:
                        temp.append(i)
                        
                        newMoves.append(temp)
                    #print(newMoves)
        moves = newMoves
    
    print(len(moves))
    #print(finalMoves)
    return len(finalMoves)
            


lines = []

with open("data12.txt") as f:
    lines = f.readlines()


caves = {}
for line in lines:
    line = line[:len(line)-1]
    two = line.split(sep='-')
    if(two[0] in caves and two[1] in caves):
        caves[two[0]].add(caves[two[1]])
        
    elif(two[0] in caves and two[1] not in caves):
        caves[two[1]] = cave(two[1])
        caves[two[0]].add(caves[two[1]])
    elif(two[0] not in caves and two[1]  in caves):
        caves[two[0]] = cave(two[0])
        caves[two[0]].add(caves[two[1]])
    elif(two[0] not in caves and two[1]  not in caves):
         caves[two[1]] = cave(two[1])
         caves[two[0]] = cave(two[0])
         caves[two[0]].add(caves[two[1]])
    else: 
        print("error")


print(search(caves))