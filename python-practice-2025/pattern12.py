heart = ''

for i in range(6):
    for j in range(7):
        if (
            (i == 0 and j % 3 != 0) or
            (i == 1 and j % 3 == 0) or
            (i - j == 2) or
            (i + j == 8)
        ):
            heart += '*'
        else:
            heart += ' '
    heart += '\n'

print(heart)

"""
 ** ** 
*  *  *
*     *
 *   * 
  * *  
   * 
"""

for i in range(1, 7):
    for j in range(1, 8):
        if (
            (i == 1 and j % 3 != 0) or     # Top two bumps
            (i == 2 and j % 3 == 1) or     # Edges of bumps
            (i - j == 2) or                # Left diagonal
            (i + j == 10)                  # Right diagonal
        ):
            heart += '*'
        else:
            heart += ' '
    heart += '\n'

print(heart)