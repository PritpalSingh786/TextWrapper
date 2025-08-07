strr = 'wow'
concate = ""

for i in range(len(strr) - 1, -1, -1):
    print(strr[i])
    concate += strr[i]

if concate == strr:
    print("Palindrome")
else:
    print("Not palindrome")
