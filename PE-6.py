__author__ = 'DMCHALE'

"""
This tool is intended to find the difference between the sum of all numbers in the given range squared and then added, and the sum all numbers in the given range added and then squared.
"""

def greater_square(n):
    a = 0
    b = 0
    for i in range(1,n+1):
        a += i * i
        b += i
    c = b * b
    difference = c - a
    print(a,b,c)
    return difference

if __name__ == '__main__':
    greater_square(input("Please enter a number to receive the difference between the sums of all numbers in that range squared then added, and added then squared: "))
