#time complexity O(n^3)

n = input()
n = int(n)

count = 0

for x in range(n):
    for y in range(n):
        for z in range(n):
            count+=1

print("n =", n,"count=",count)