strr = ""
for row in range(5, 0, -1):
    for col in range(1, row + 1):
        strr += str(row) + " "
    strr += "\n"

print(strr)

"""
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
"""
