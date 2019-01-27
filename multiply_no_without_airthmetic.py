#!/usr/bin/python

# Program to multiply two numbers without using airthmetic operator

def add_nos(x, y):
    carry_in, temp_y, temp_x, index, sum_ = 0, y, x, 1, 0
    while temp_y:
        # either both digits are set to 1 or either there is already a carry
        carry_out = (x & carry_in) | ((y & index) & (x & index)) | (y & carry_in)

        # sum
        sum_ |= carry_in ^ x ^ y

        # shift carry to add to next no
        carry_in, temp_y, temp_x, index = (carry_out << 1, temp_y >> 1, temp_x >> 1, index << 1)
    return sum_ | carry_in


no1 = int(input("Enter first no : "))
no2 = int(input("Enter second no : "))

sum_ = 0
while no1:
    if no1 & 1:
        sum_ = add_nos(sum_, no2)
    no1 = no1 >> 1
    no2 = no2 << 1

print("Multiplication is : ", sum_)
