# 利用條件運算符的嵌套來完成此題(完成)
# 學習成績>=90分的同學用A表示
# 60-89分之間的用B表示
# 60分以下的用C表示
score = int(input("請輸入學習成績:"))
if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")
