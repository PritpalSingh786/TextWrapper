strr = ""
initial_value = 15
for row in range(5, 0, -1):
    for col in range(1, row + 1):
        strr += str(initial_value) + " "
        initial_value -= 1
    strr += "\n"

print(strr)

"""
15 14 13 12 11 
10 9 8 7 
6 5 4 
3 2 
1 
"""
