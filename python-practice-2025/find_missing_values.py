arr = [1, 10, 7]

min_value = arr[0]
max_value = arr[0]

# Find min and max
for i in range(1, len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]
    if arr[i] < min_value:
        min_value = arr[i]
    print(min_value)

print("Max:", max_value)
print("Min:", min_value)

# Find and print missing numbers between min and max
for j in range(min_value, max_value + 1):
    found = False
    for i in range(len(arr)):
        if arr[i] == j:
            found = True
            break
    if not found:
        print("Missing:", j)
