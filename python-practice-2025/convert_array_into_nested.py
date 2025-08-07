array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
arr1 = []
arr2 = []
chunks = 5

for i in range(len(array)):
    arr1.append(array[i])
    if len(arr1) == chunks:
        arr2.append(arr1)
        arr1 = []

if len(arr1) > 0:
    arr2.append(arr1)

print(arr2)
