array = [2,5,1,9,7,8,3,0,6,4]
n = len(array)
print(array)

for i in range(0, n-1):
    for j in range(n-1, i, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]

print(array)
