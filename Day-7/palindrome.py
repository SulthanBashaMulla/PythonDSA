#To check the reverse of a number -- palindrome or not
#TC --> 0(log10(N))
#SC --> 0(1)

n = int(input("Enter a number you want to check: "))
num = n
result = 0
while num > 0:
    last_d = num%10
    result = (result*10)+last_d
    num = num//10
if n == result:
    print(f"{n}, is a palindrome")
else:
    print(f"{n}, is not a palindrome")