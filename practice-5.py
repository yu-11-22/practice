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
