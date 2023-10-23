# using sep to separate the numbers
print(5,6,7, sep='*', end=' ')
# using sep for strings
print("helo","world",sep=' ',end=' ')
# variables starts with letter only,no space,no limits,give underscore,combination of nums,keywords cant be used as var
name="vijaya"
print(name)
num=6
print(num)
print(type(num))
#input and output statements(import is a keyword
import math
a=int(input('enter value of a:'))
b=int(input('enter value of b:'))
print('addition',a+b)
print('subtraction',a-b)
print('division',a/b)
print('multiplication',a*b)
#define class
class bike:
    name="MT15"
    gear=4
#craeting objects of a class
bike1=bike()
# access attr and assign new values
bike1.name="duke"
bike1.gear=3
print(f"fusion{bike1}")

