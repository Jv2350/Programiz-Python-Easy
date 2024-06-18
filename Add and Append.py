# Write a function to create a function that adds two numbers and appends the result.

def add_numbers(num1, num2):
    if num1==0 and num2==0:
        return 0
    else:
        return (f"{num1}{num2}{num1+num2}")
