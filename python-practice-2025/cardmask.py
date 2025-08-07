card_number = "4111111111111111"
length_of_card_number = len(card_number)

# Get first and last characters
first_char = card_number[0]
last_char = card_number[length_of_card_number - 1]

# Slice the middle portion and replace all characters with 'X'
remove_first_and_last = card_number[1:-1]
masked = ''.join('X' for _ in remove_first_and_last)

# Concatenate the final masked card
final_masked_card = first_char + masked + last_char
print("Masked Card:\n", final_masked_card)

# Without using built-in methods
mask = ""
for i in range(len(card_number)):
    if i == 0 or i == len(card_number) - 1:
        mask += card_number[i]
    else:
        mask += "X"

print(mask)
