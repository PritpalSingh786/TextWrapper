n = 121
temp = n
result = 0

while n > 0:
    remainder = n % 10
    result = result * 10 + remainder
    n = n // 10  # floor division

if result == temp:
    print("Palindrome")
else:
    print("Not palindrome")
