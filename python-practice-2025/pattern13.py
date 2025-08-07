strr = ""
for row in range(1, 6):
    for col in range(row, 5):
        strr += " "
    for col in range(1, 2 * row):
        strr += "*"
    strr += "\n"

print(strr)

'''

    *
   ***
  *****
 *******
*********

'''