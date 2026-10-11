# Counting No.of digits in a number

n = int(input("Enter a number: "))
num = n
count = 0
while num>0:
    num = num//10
    count += 1
print("No.of digits in the number", n,"is", count)