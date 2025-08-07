# Initial list with duplicate values
data_list = [1, 1, 1, 1, 2, 2, 2, 1, 2, 3, 1, 11, 12, 100, 1, 5, 7, 7, 112, 112, 123]

while True:
    current_length = len(data_list)
    print(current_length)  # Debugging: current length

    for i in range(len(data_list)):
        item = data_list[i]

        try:
            first_index = data_list.index(item)
            next_index = data_list.index(item, first_index + 1)

            # If found again, remove the duplicate
            data_list.pop(next_index)
            break  # Restart the loop after removal
        except ValueError:
            pass  # No duplicate found for this item

    if len(data_list) == current_length:
        break  # No elements removed, exit loop

# Final list with one occurrence of each element
print("Deduplicated List:", data_list)

# Manually create a unique list (like JS nested loop)
unique_list = []

for i in range(len(data_list)):
    is_duplicate = False
    for j in range(len(unique_list)):
        if data_list[i] == unique_list[j]:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_list.append(data_list[i])

print("Unique List:", unique_list)
