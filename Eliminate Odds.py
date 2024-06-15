# Write a function to eliminate all odd numbers from a given list.
# Instructions
# Return the new list of even numbers.


def eliminate_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
