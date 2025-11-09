n = 1234321

def checkPalindrome(n):
    num = n
    digit = 0
    while num>0:
        ld = num%10
        digit = digit*10 + ld
        num = num//10
    
    return n == digit

print(checkPalindrome(n))

# print(digit)

# if n == digit:
#     print("given number is palindrome")
# else:
#     print('given number is not palindrom')
