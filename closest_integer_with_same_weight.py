#!/usr/bin/python

# Program to find the closest integer with same weight ex: 7 = 111 in binary has weight=3(no. of bits set) so it's closest integer is 11 (1011)


number = int(input("Enter a decimal no : "))

max_bit_size = 64

def find_closest_integer_with_same_weight(x):
    for i in range(max_bit_size -1):
        if (x >> i)& 1 != (x >> (i+1))&1:
            x ^= (1 << i)| (1 << (i+1))
            return x
    return None

return_value = find_closest_integer_with_same_weight(number)
if return_value:
    print("Closest integer is : {}".format(return_value))
else:
    raise ValueError("All bits are wither 0 or 1")
        
