strr = ''
for i in range(4):
    for j in range(i, 4):
        strr += " "  # add space for left padding
    for j in range(i + 1):
        strr += "*"
    strr += "\n"

print(strr)

"""
    *
   **
  ***
 ****
"""
