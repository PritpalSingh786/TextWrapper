strr = ''
for i in range(6, 0, -1):
    for j in range(1, i):
        strr += str(j) + " "
    strr += "\n"

print(strr)

"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
