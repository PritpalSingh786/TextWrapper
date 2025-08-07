count = {}
arr = [3, 3, 2, 2, 5, 5]

for i in range(len(arr)):
    if arr[i] not in count:
        count[arr[i]] = 1
    else:
        count[arr[i]] += 1

print(count)
