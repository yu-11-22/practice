# 正方形乘機
for i in range(1, 10):
    print(("%3d") % (i), end="")
    for j in range(1, 10):
        print(("%3d") % (j*i), end="")
    print(end="\n")
