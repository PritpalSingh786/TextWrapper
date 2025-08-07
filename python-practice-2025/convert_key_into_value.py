dictt = {1:'a', 2:'b'}
dictt1 = {}

for k, v in dictt.items():
    dictt1.setdefault(v, []).append(k)
print(dictt1)