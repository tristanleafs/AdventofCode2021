from collections import Counter

#panick change
lines = ""

with open("data7.txt") as f:
    lines = f.readline()

dists = [int(s) for s in lines.split(sep=",")]

#did not work
#orginally going to have all the crabs move to the most common location
# counter_thing = Counter(dists)
# most =  counter_thing.most_common(1)[0][0]

#could have just been the first value but I used a large value in to write it quicker
cost = 3859390000

#probably could have used a better way to decide the range to check
for k in range(2000):
    temp = 0
    for i in dists:
        temp += sum(range(abs(i-k)+1))
        
        #only code change from part 1
        #temp += abs(i-k)
    if(temp < cost):
        cost = temp

#takes about 20 seconds to process so this is not an ideal solution

# print(most)
print(cost)