arr = [121, 456]

for i in arr:
    result = 0
    temp = i
    while temp > 0:
        mod = temp % 10
        result = result * 10 + mod
        temp = temp // 10
    if result == i:
        print(i)
