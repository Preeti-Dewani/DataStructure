#!/usr/bin/python

# Program to find x raise to y

x = int(input("Enter value of x : "))
power = int(input("Enter value of y : ")) - 1
result = x

while power:
    if power & 1:
        result *= x
    x, power = x*x, power >> 1

print("Result is : ", result)
