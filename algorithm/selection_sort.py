array = [4,2,7,8,0,5,1,3,6,9]
n = len(array)
print(array)

for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if array[j] < array[min]:
            min = j
    tmp = array[i]
    array[i] = array[min]
    array[min] = tmp

print(array)
