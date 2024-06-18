# Write a function to calculate the sum of all even numbers in a matrix.


def sum_of_evens(matrix):
    sum = 0
    for i in matrix:
        for j in i:
            if j % 2 == 0:
                sum += j

    return sum
