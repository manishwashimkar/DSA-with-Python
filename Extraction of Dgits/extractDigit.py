# num = 587345675467
# count = 0

# while num>0 :
#     last_digit = num%10
#     print(last_digit)
#     num = num//10
#     count+= 1

# print(count)


# CHECK PALIDROME

n = 153
num = n
count = 0
result = 0

while num > 0:
    ld = num % 10
    result = (result * 10) + ld
    num = num // 10
    count += 1

if result == n:
    print("Its a Palindrome")
else:
    print("Not a Palindrome")

print(count)
print(result)

