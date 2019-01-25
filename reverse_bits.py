#!/usr/bin/python

# Program to reverse bits

number = int(input("Enter a number : "))

def reverse_bits(number):
    max_bits_size = 4
    for i in range(max_bits_size//2):
        if (number >> i)&1 != (number >> (max_bits_size - i -1))&1:
            number ^= (1 << i) | (1 << (max_bits_size-i-1))
    return number

reversed_no = reverse_bits(number)
print("Reversed no is : {}".format(reversed_no))
