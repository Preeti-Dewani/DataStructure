#!/usr/bin/python

# Program to calculate the parity of number

number = int(input("Enter a no to calculate parity : "))
actual_no = number

# version 1 : with if condition

number_of_bits = 0
while number:
    number_of_bits += number & 1
    number=number >> 1

parity = 1 if (number_of_bits == 1 or number_of_bits % 2 !=0) else 0
print("Parity of number {number} is : {parity}".format(number=actual_no, parity=parity))



# version 2: without if condition
number = actual_no
parity = 0
while number:
    parity ^= number & 1
    number >>= 1

print("Parity of number {number} is : {parity}".format(number=actual_no, parity=parity))
