num = 12348563525475
count = 0

while num >0:
    count+=1
    num = num//10

print(count)

# for negative numbers
num2 = -9876
count2 = len(str(abs(num2)))
print(count2)   # Output: 4

# using log10 By importing math

import math

x = -7636483
num3=abs(x)
count3 = math.floor(math.log10(num3)) +1
print(count3)
