def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]
    return "not found"

print(two_sum([1, 2, 4], 3))

