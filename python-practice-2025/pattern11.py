strr = ""
for i in range(1, 6):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            strr += "1 "
        else:
            strr += "0 "
    strr += "\n"

print(strr)

"""
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
"""
