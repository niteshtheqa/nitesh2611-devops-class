# Question 7: Return the total count of sub-string “Emma”
# appears in the given string
def count_substring(input_string, sub_string):
    return input_string.count(sub_string)


print(count_substring('Emma is good developer. Emma is a writer', 'Emma'))


