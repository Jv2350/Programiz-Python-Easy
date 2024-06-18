# Write a function to find the sum Of the two smallest numbers in a list.


def sum_of_smallest(numbers):
    min1 = min(numbers)
    numbers.remove(min1)
    min2 = min(numbers)

    return min1 + min2
