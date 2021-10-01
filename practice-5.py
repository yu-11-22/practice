# 輸入三個整數x,y,z，請把這三個數由小到大輸出(完成)
x = int(input("x值:"))
y = int(input("y值:"))
z = int(input("z值:"))
if x > y:
    if x > z:
        if y > z:
            print(z, y, x)
        else:
            print(y, z, x)
    else:
        print(y, x, z)
else:
    if y > z:
        if x > z:
            print(z, x, y)
        else:
            print(x, z, y)
    else:
        print(x, y, z)

# 範例
l = []
for i in range(3):
    x = int(input("integer:\n"))
    l.append(x)     # append把串列當成一個元素放進去
l.sort()            # sort會對文字做排序(改成由大到小,在列表中加入reverse=True)
print(l)
