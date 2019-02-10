#!/usr/bin/python

# Program to divide two numbers using only +, -, and bitwise

# Performing x/y operation

x = int(input("Enter number 1 :"))
y = int(input("Enter number 2 : "))
actual_y = y

def find_quotient(x, y):
    if x < y or x == y:
        return 0

    while y<x:
        y = y << 1

    nearest_integer = y-x if  (y - x) < x - (y >>1) else x - (y >>1) 
    print("nearest integer : ", nearest_integer)
    while nearest_integer >= actual_y:
        nearest_integer -= actual_y
        
    return no_of_runs


print("QUOTIENT RECEIVED IS : ", find_quotient(x, y))
