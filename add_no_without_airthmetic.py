#!/usr/bin/python

# Program to add two numbers without using airthmetic operator

def add_nos(x, y):
    carry_in, temp_y, temp_x, index, sum = 0, y, x, 1, 0
    while temp_y:
        # either both digits are set to 1 or either there is already a carry
        carry_out = (x & carry_in) | ((y & index) & (x & index)) | (y & carry_in)

        # sum
        sum |= carry_in ^ x ^ y

        # shift carry to add to next no
        carry_in, temp_y, temp_x, index = (carry_out << 1, temp_y >> 1, temp_x >> 1, index << 1)
    return sum | carry_in


no1 = int(input("Enter first no : "))
no2 = int(input("Enter second no : "))
print(add_nos(no1, no2))
