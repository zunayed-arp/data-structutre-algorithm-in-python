#time and space complexity O(n)
n = 100

even = [False] * (n+1)

for i in range(0,n+1,2):
    even[i] = True

'''
>>>even[2]
True
>>>even[3]
False
>>>even[99]
False
>>>even[100]
True
'''