#!/usr/bin/python3
""" write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file. """

def minOperations(n):
    if n == 1:
        return 0  # Already have a single 'H' character
    
    operations = 0
    clipboard = 1  # Initially, we have a single 'H' character in the file
    
    while clipboard < n:
        if n % clipboard == 0:
            clipboard = n  # If n is divisible by the clipboard, we can directly reach n
        else:
            operations += 1  # Perform a copy and paste operation
            clipboard *= 2  # Double the number of 'H' characters in the file
    
    return operations
