# 一球從100米高度自由落下，每次落地後反跳回原高度的一半；再落下
# 求它在第10次落地時，共經過多少米？第10次反彈多高？
sum = 0
n = 100
for m in range(1, 11):
    ans = n+(n/2)
    n = n/2
    sum += ans
dis = sum-n
print("共經過%f米" % dis, end=" ")
print("第十次反彈高度:", n)
