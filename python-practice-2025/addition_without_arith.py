def add(a, b):
    while b != 0:
        carry = a & b       # carry
        a = a ^ b           # sum without carry
        b = carry << 1      # shift carry
    return a

print(add(5, 3))  # Output: 8

'''
Bitwise AND (&) and XOR (^) Rules
| A | B | A & B | A ^ B |
|---|---|--------|--------|
| 0 | 0 |   0    |   0    |
| 0 | 1 |   0    |   1    |
| 1 | 0 |   0    |   1    |
| 1 | 1 |   1    |   0    |

step1:
carry = a & b = 5 & 3 = 8421 = 0101 & 0011 = 0001 = 1
a = a ^ b = 8421 = 0101 ^ 0011 = 0110 = 6
b = carry << 1 = 0001 << 1 = 0010 = 2

step2:
carry = a & b = 6 & 2 = 8421 = 0110 & 0010 = 0010 = 2
a = a ^ b = 6 ^ 2 = 8421 = 0110 ^ 0010 = 0100 = 4
b = carry << 1 = 0010 << 1 = 0100 = 4

step3:
carry = a & b = 4 & 4 = 8421 = 0100 & 0100 = 0100 = 4
a = a ^ b = 4 ^ 4 = 8421 = 0100 ^ 0100 = 0000 = 0
b = carry << 1 = 0100 << 1 = 1000 = 8

step4:
carry = a & b = 0 & 8 = 8421 = 0000 & 1000 = 0000 = 0
a = a ^ b = 0 ^ 8 = 8421 = 0000 ^ 1000 = 1000 = 8
b = carry << 1 = 0000 << 1 = 0000 = 0

when b == 0 then return a = 8
'''
