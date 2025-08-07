arr = [0,1,2,3]
isFind = False

for i in arr:
    if(i<2):
        continue
    else:
       isPrime = True
       for j in range(2,i):
          if i%j==0:
            isPrime = False
            break
    if(isPrime):
       print(i)
       isFind = True
if(not isFind):
   print('not found')