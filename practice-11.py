# 有一對兔子，從出生後第3個月起每個月都生一對兔子(完成)
# 小兔子長到第三個月後每個月又生一對兔子
# 假如兔子都不死，問每個月的兔子總數為多少？
# 1 1 2 3 5 8 13...
n = int(input("幾個月起:"))
l = []
f1 = 1
f2 = 1
for i in range(0, n):
    if n == 1:
        x = 1
        break
    elif n == 2:
        x = 2
        break
    else:
        f1 = f1+f2
        f2 = f1+f2
        l.append(f1)
        l.append(f2)
        x = 2+sum(l[0:n-2])
print("n個月後的兔子總數:", x)


# 範例
f1 = 1
f2 = 1
for i in range(1, 22):
    print(("%12ld %12ld") % (f1, f2), end="")   # %ld長整數
    if (i % 3) == 0:
        print("")
    f1 += f2
    f2 += f1
