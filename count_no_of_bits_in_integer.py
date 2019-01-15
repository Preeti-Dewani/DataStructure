#!/usr/bin/python

# Program to count no. of bits in an integer

import sys

# to parse the no from command line
number = int(sys.argv[1])
actual_no = number

# counter to count no of bits
number_of_bits = 0

# version 1
# loop to execute main logic
while number:
    if number & 1:
        number_of_bits += 1
    number = number >> 1


print("No. of bits in no: {number} are : {bits}".format(number=actual_no, bits=number_of_bits))

# version 2 implementation: without using if

number = actual_no
number_of_bits = 0

while number:
    number_of_bits += number & 1
    number = number >> 1


print("No. of bits in no: {number} are : {bits}".format(number=actual_no, bits=number_of_bits))
