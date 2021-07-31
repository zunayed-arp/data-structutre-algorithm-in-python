#time complexity O(n)

n = input()
n = int(n)

count = 0
for i in range(n):
    count+=1
for i in range(n):
    for y in range(n):
        count+=1

print("n =", n,"count =",count)