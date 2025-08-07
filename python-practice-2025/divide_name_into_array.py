name1 = "pritpal"
arr = []

for i in range(len(name1), 0, -1):
    str_ = ''
    for j in range(i):
        str_ += name1[j]
    arr.append(str_)

print(arr)
