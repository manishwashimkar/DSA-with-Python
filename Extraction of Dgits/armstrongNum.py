# CHECK ARMSTRONG
n = 153
num2 = n
total = 0
while num2 > 0:
    old = num2 % 10
    total += old ** len(str(n))  # can also use count
    num2 = num2 // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not armstrong number")


print(len(str(n)))
