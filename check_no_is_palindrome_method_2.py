#!/usr/bin/python

# Program to check no is palindrome or not

import math

def is_palindrome_no(number):
    no_of_digits = math.floor(math.log10(number)) + 1
    msb_mask = 10 ** (no_of_digits-1)
    for i in range(no_of_digits // 2):
        lsb = number % 10
        if number // msb_mask != lsb:
            return False

        number = number % msb_mask
        number = number // 10
        msb_mask = msb_mask // 100    
    return True

number = int(input("Enter a no : "))
result = is_palindrome_no(number)
print("Result is : ", result) 
