#Time complexity O(n)

n = input()

n = int(n)
result = 0
for x in range(1,n-1):
    result = result+x

print(result)