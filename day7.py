from collections import Counter


lines = ""
with open("data7.txt") as f:
    lines = f.readline()

dists = [int(s) for s in lines.split(sep=",")]

# counter_thing = Counter(dists)
# most =  counter_thing.most_common(1)[0][0]

cost = 3859390000
for k in range(2000):
    temp = 0
    for i in dists:
        temp += sum(range(abs(i-k)+1))
    if(temp < cost):
        cost = temp

# print(most)
print(cost)