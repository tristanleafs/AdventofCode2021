# def calcValue(arr, position):
#     val = 0
#     for i in arr:
#         val += sum(range(abs(i-position)+1))
#     return val

# def findMin(arr, low, high):
#     # This condition is needed to handle the case when array is not
#     # rotated at all
#     # if high < low:
        
#     #     return calcValue(arr, low)
 
#     # If there is only one element left
#     if high == low:
#         return low
 
#     # Find mid
#     mid = int((low + high)/2)
 
#     # Check if element (mid+1) is minimum element. Consider
#     # the cases like [3, 4, 5, 1, 2]
#     if mid < high and  calcValue(arr ,mid+1) <  calcValue(arr, mid):
#         return mid+1
 
#     # Check if mid itself is minimum element
#     if mid > low and calcValue(arr, mid) < calcValue(arr ,mid-1):
#         return mid
 
#     # Decide whether we need to go to left half or right half
#     if calcValue(arr, high) > calcValue(arr, mid):
#         return findMin(arr, low, mid-1)
#     return findMin(arr, mid+1, high)

#unfortunatley binary search does not work for this problem


#panick change
lines = ""

with open("data7.txt") as f:
    lines = f.readline()

dists = [int(s) for s in lines.split(sep=",")]


#could have just been the first value but I used a large value in to write it quicker
cost = 3859390000

# probably could have used a better way to decide the range to check
for k in range(2000):
    temp = 0
    for i in dists:
        #using mathematical sum is faster
        n = abs(i-k)
        temp += int((n/2)*(1+n))
        
        #only code change from part 1
        #temp += abs(i-k)
    if(temp < cost):
        cost = temp

#now takes 1 second to compute




ans = 95851339
print(cost)
print("This code works:" ,ans == cost)