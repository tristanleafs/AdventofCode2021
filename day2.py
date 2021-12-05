
lines = []
with open("data2.txt") as f:
    lines = f.readlines()

depth = 0
dist = 0
actualDepth = 0


for line in lines:
    if("forward" in line): 
         shit = [int(s) for s in line.split() if s.isdigit()]
         dist += shit[0]
         actualDepth += depth*shit[0]
    elif("down" in line): 
        shit = [int(s) for s in line.split() if s.isdigit()]
        depth += shit[0]
    elif("up" in line): 
        shit = [int(s) for s in line.split() if s.isdigit()]
        depth -= shit[0]
    else:
        print("error")

print("depth", depth)
print("dist", dist)
print("ans:", actualDepth*dist)