# Question 4: Given a string and an integer number n, remove characters from a
# string starting from zero up to n and return a new string
def remove_string_to_number(input_string, number_of_chars):
    return input_string[number_of_chars:]


input_string1 = input('Enter the string: ')
number_of_characters = int(input('Enter the number of chars to remove: '))
print(remove_string_to_number(input_string1, number_of_characters))

