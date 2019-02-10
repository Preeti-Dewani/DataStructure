#!/usr/bin/python

# Program to check no is palindrome

number = int(input("Enter the number : "))

def check_no_is_palindrome(number):
    result, remaining = 0, abs(number)
    while remaining:
        result = result * 10 + remaining % 10
        remaining //= 10
    return "yes" if number == result else "no"

print("No {} is palindrome : {}".format(number, check_no_is_palindrome(number)))
