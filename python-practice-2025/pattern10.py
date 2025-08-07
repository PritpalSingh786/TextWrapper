strr = ""
initial_value = 1
for row in range(1, 6):
    for col in range(1, row + 1):
        strr += str(initial_value) + " "
        initial_value += 1
    strr += "\n"

print(strr)

"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""
