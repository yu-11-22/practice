# 將一個正整數分解質因數。例如：輸入90,打印出90=2*3*3*5
while 1:
    n = int(input("輸入一個正整數:"))
    print("%d=" % n, end="")
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                n = int(n/i)
                if n == 1:
                    print("%d" % i, end="\n")
                else:
                    print("%d*" % i, end="")
                break
    break
