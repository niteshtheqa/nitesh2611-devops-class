# Question 3: Given a string, display only those characters which are present at an
# even index number.

def print_even_character_from_string(input_string):
    str_length = len(input_string)
    print('Length of String:{}'.format(str_length))
    for i in range(0, str_length-1, 2):
        print("[Index", i, "]", input_string[i])





print_even_character_from_string("wayafalkar")