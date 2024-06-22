# Write a function to calculate the nth triangular number.
# Instructions
# A triangular number is calculated by adding all natural numbers up to n.
# Return the nth triangular number.


def triangular_number(n):
    sum = 0
    for i in range(n + 1):
        sum += i

    return sum
