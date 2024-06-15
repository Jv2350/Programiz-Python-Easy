# Write a function to find the largest number that can be formed by
# swapping two digits of a given number.
# Instructions
# Swap the two digits of the number and compare it with the original number.
# If it's larger, return it; otherwise, return the original number.


def largest_swap(num):
    numStr = str(num)
    swap = numStr[::-1]
    swapNum = int(swap)

    return max(num, swapNum)
