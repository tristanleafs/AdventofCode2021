def countMatch(str1, str2):
    '''counts the number of common characters between two strings
    assuming the strings have only unique characters'''
    sum = 0
    for i in str1:
        if(i in str2):
            sum += 1
    return sum

def decode(codes, word):
    '''finds the value associated with a word and codes'''
    for i, test in enumerate(codes):
        if(len(test) == len(word)):
            valid = True
            for char in word:
                if(char not in test):
                    valid = False
            if(valid): return i
    print("error")
    print(codes)
    print(word)
    return -1

lines = []
with open("data8.txt") as f:
    lines = f.readlines()
#part 1
#1 4 7 8

#1 -> 2 
#2
#4 -> 4
#7 -> 3
#8 -> 7

output = []
input = []
for line in lines:
    line = line.split()
    output.append(line[11:])
    input.append(line[:11])

sum = 0
for line in output:
    for command in line:
        if(len(command) == 2 or
        len(command) == 4 or
        len(command) == 3 or
        len(command) == 7 ):
            sum +=1

print("part 1 ans:" ,sum)

#part 2
sum = 0
for line, outputLine in zip(input, output):
    codes = ["","","","","","","","","",""]
    
    #check input for unique digits
    for command in line:
        if(len(command) == 2):
            
            codes[1] = command
        elif(len(command) == 4):
           
            codes[4] = command
        elif(len(command) == 3):
           
            codes[7] = command
        elif(len(command) == 7):
           
            codes[8] = command
    
    #find other digits by half assed deduction
    for command in line:
        if(len(command) == 2 or
        len(command) == 4 or
        len(command) == 3 or
        len(command) == 7 ):
            pass
            
        else:
            #9 is the only digit to share four codes with 4
            if(countMatch(command, codes[4]) == 4):
                codes[9] = command 
            #kinda just had to use a bunch of relationships with 0 to find it
            elif(countMatch(command, codes[4]) == 3 and countMatch(command, codes[1]) == 2 and countMatch(command, codes[8]) == 6):
                codes[0] = command
            #6 is the last digit with one fewer codes in common with 8
            elif(countMatch(command, codes[8]) == 6):
                codes[6] = command
            #3 is the last code to countain all of one at this point
            elif(countMatch(command, codes[1]) == 2):
                codes[3] = command
            #through elimination 5 will only have 3 codes in common with 4
            elif(countMatch(command, codes[4]) == 3):
                codes[5] = command
            #the last option is 2 which has 2 codes in common with 4
            elif(countMatch(command, codes[4]) == 2):
                codes[2] = command
            #I have no idea what ends up here, but some do
            else:
                pass

    #decode output
    sum += decode(codes, outputLine[0])*1000
    sum += decode(codes, outputLine[1])*100
    sum += decode(codes, outputLine[2])*10
    sum += decode(codes, outputLine[3])


print("part 2 ans:", sum)

#0 -> 6
#1 -> 2 
#2 -> 5
#3 -> 5
#4 -> 4
#5 -> 5
#6 -> 6
#7 -> 3
#8 -> 7
#9 -> 6
