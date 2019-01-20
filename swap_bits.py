#!/usr/bin/python

# Program to swap bits

number = int(input("Enter the number : "))
first_index = int(input("Enter the first index to be swapped : "))
second_index = int(input("Enter the second index to be swapped : "))

bit_at_first_index = (number >> first_index) & 1
bit_at_second_index = (number >> second_index) & 1

if bit_at_first_index != bit_at_second_index: 
    number = number ^ (1 << second_index)
    number = number ^ ( 1 << first_index)

print("Number after bits swapped is : {}".format(number))
