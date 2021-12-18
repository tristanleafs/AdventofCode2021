
# def search(line, index, open):
#     char = line[index]
#     badChar = None
#     while(char != "\n" and badChar == None):
#         if (char in openers):
#             badChar = search(line, index+1, char)
#         else:
#             if(char == flip[open]):
#                 return None
#             else:
#                 return char
#         index += 1
#         char = line[index]
#     return badChar

# def search(line):
#     opens = 0
#     closes = 0
#     for i in range(len(line)):
#         open = line[i]
#         if(open in openers):
#             opens = 0
#             closes = 0
#             for k in range(i+1, len(line)):
#                 if(line[k] in openers):
#                     opens += 1
#                 elif(line[k] in closers):
#                     closes += 1
#                 else:
#                     #print("fuck")
#                     pass
#                 if(opens == closes):
#                     if(open != flip[line[k]]):
#                         print("Test", open, line[k])
#                         print(i, k)
#                         print(line)
#                         return line[k]
#     return None

import copy

def search(line):
    temp = copy.deepcopy(line)
    #print(line)
    count = 0
    while(len(temp) and count < 50):
        for i in range(len(temp)-1):
            if(temp[i] in openers and temp[i+1] in closers):
                if(temp[i] == flip[temp[i+1]]):
                    temp = temp[:i] + temp[i+2:]
                    break
                else:
                    return temp[i+1]
        count+=1
    return None

def search2(line):
    temp = copy.deepcopy(line)
    #print(line)
    count = 0
    while(len(temp) and count < 50):
        for i in range(len(temp)-1):
            if(temp[i] in openers and temp[i+1] in closers):
                if(temp[i] == flip[temp[i+1]]):
                    temp = temp[:i] + temp[i+2:]
                    break
                else:
                    return temp[i+1]
        count+=1

    scoreVal = 0

    for i in range(len(temp)-2, -1, -1):
        scoreVal *= 5
        scoreVal += score2[flip[temp[i]]]
        #print(flip[temp[i]] , end="")
        
    #print()
    return scoreVal
    


lines = []
with open("data10.txt") as f:
    lines = f.readlines()

score = {
    ')': 3,
    '(': 3,
']': 57,
'[' : 57,
'}': 1197,
'{': 1197,
'<' : 25137,
'>': 25137,
None : 0
}

score2 = {
    ')': 1 ,
']': 2 ,
'}': 3 ,
'>': 4 
}

flip = {
    '(' : ')',
    ')' : '(',
    '{' : '}',
    '}' : '{',
    '[' : ']',
    ']' : '[',
    '<' : '>',
    '>' : '<'
}

openers = ['(', '{', '[', '<']
closers = [')', '}', ']', '>']

#check for corruption
sum = 0
incompletes = []
for line in lines:
    corrupt = False
    badChar = search(line)
    sum += score[badChar]

    if(badChar == None):
        incompletes.append(search2(line))

print("part 1 ans:", sum)
#print(incompletes)
incompletes.sort()
#print(incompletes)
print("part 2 ans:" ,incompletes[int(len(incompletes)/2)])