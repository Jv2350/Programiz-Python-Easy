# # Write a function to find the index of the first vowel in a given string.
# Instructions
# Return the index of the first vowel in the string. If there are no vowels, return -1.


def first_vowel_index(s):
    vowels = "aeiouAEIOU"
    for index, char in enumerate(s):
        if char in vowels:
            return index
    return -1
