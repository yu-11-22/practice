# 輸入某年某月某日，判斷這一天是這一年的第幾天？
y = int(input("輸入年:"))
m = int(input("輸入月:"))
d = int(input("輸入日:"))
ms = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
error = ("data error")
if d > 31:
    print(error)
elif m > 12:
    print(error)
elif d > 30 and (m == 4 or m == 6 or m == 9 or m == 11):
    print(error)
elif m == 2 and d > 29:
    print(error)
elif y % 4 != 0 and m == 2 and d > 28:
    print(error)
elif y % 4 != 0 and 0 < m <= 12:
    print(ms[m-1]+d)
elif y % 4 == 0 and 2 < m <= 12:
    print(ms[m-1]+1+d)
elif y % 4 == 0 and m <= 2:
    print(ms[m-1]+d)
else:
    print(error)
