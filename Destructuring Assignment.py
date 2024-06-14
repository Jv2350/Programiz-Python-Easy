# Write a function to swap the values Of two variables using destructuring assignment.


def swap_values(a, b):
    temp = a
    a = b
    b = temp

    return (a, b)
