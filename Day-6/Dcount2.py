#v2 of counting the digits in a num

from math import *
n = int(input("Enter the number: "))
num = n
def countdigits(num):
    return int(log10(num)+1)
print("No.of digits in", n, "is", countdigits(num))