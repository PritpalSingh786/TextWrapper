arr = [1, 6, 8, 5]
for i in range(len(arr)):
    for j in range(len(arr) - 1):  # avoid IndexError at j+1
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
