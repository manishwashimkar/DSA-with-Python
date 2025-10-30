num = 587345675467
count = 0

while num>0 :
    last_digit = num%10
    print(last_digit)
    num = num//10
    count+= 1

print(count)