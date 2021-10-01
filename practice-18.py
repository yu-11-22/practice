# 求 s = a + aa + aaa + aaaa + aa ... a 的值
# 例如 a 是一個數字。 2 + 22 + 222 + 2222 + 22222（目前共有 5 個數字相加）
# 幾個數相加由鍵盤控制
n = int(input("幾個數:"))
a = int(input("a值:"))
sum = 0
for i in range(0, n):
    a = a*10
    sum += a
ans = sum/10
S = 0
for j in range(1, n+1):
    A = ans//(10**(j-1))
    S += A
print(S)
