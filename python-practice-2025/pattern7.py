strr = ""
for i in range(4):
    for j in range(5):
        if i == 0 or i == 3 or j == 0 or j == 4:
            strr += "*"
        else:
            strr += " "
    strr += "\n"

print(strr)

"""
*****
*   *
*   *
*****
"""
