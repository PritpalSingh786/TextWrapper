def binary_search(arr, key):
    arr.sort()  # Sort the array just like JS sort((a, b) => a - b)
    low = 0
    high = len(arr) - 1
    is_found = False

    while low <= high and not is_found:
        mid = (low + high) // 2  # floor division
        if arr[mid] == key:
            is_found = True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    if is_found:
        print(f"Key {key} found at index {mid}")
    else:
        print("Key not found")

# Test
arr = [2, 1, 4]
binary_search(arr, 1)
