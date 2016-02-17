__author__ = 'DMCHALE'

"""
This tool is intended to find the smallest number that is divisible by all real numbers within a given range.
"""

def range_divisible(n):
    all_divisible = True
    i = 1
    working_list = []
    while all_divisible is True :
        for number in range(1,n+1):
            if i % number == 0:
                working_list.append(number)
                if len(working_list) == n:
                    print(str(i) + " is divisible by all real numbers from 1 to "  + str(n) + ".")
                    all_divisible = False
                continue
            else:
                working_list = []
                i+= 1
                pass

if __name__ == '__main__':
    range_divisible(input("Please enter a number to receive the lowest number divisible by all real numbers from 1 to your number: "))