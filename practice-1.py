# 有四個數字:1,2,3,4
# 組成多少個互不相同且無重複數字的三位數
# 各數是多少?
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if (a != b) and (a != c) and (b != c):
                print(("%d,%d,%d") % (a, b, c))
