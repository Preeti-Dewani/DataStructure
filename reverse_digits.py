#!/usr/bin/python

# program to reverse digits 42 to 24

number = int(input("Enter the no to reverse : "))

def reverse_digits(number):
    result, remaining = 0, abs(number)

    while remaining:
        result = result * 10 + remaining % 10
        remaining = remaining // 10

    return -result if number < 0 else result

print(" Reverse no is : ", reverse_digits(number))
