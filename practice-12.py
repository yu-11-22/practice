# 判斷101-200之間有多少個素數，並輸出所有素數
from sys import stdout
from math import sqrt
l = []
for x in range(101, 200):
    for y in range(2, x-1):
        if x % y == 0:
            break
    else:
        l.append(x)
print(l)
print("總數為:", len(l))
# 範例(未解)
h = 0
leap = 1
for m in range(101, 201):
    k = int(sqrt(m+1))
    for i in range(2, k+1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print("%-4d" % m)
        h += 1
        if h % 10 == 0:
            print("")
    leap = 1
print("Total is %d" % h)
