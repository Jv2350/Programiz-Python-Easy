# Write a function to calculate the sum of even numbers from a given list.


def sum_of_evens(numbers):
    sum = 0
    for i in numbers:
        if i % 2 == 0:
            sum += i

    return sum
