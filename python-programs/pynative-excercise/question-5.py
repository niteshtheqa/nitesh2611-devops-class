# Question 5: Given a list of numbers, return True if first and last number
# of a list is same
def first_last_number_same(list1):

    list_len = len(list1)
    if list1[0] == list1[list_len - 1]:
        return True
    else:
        False


_list1 = [10, 20, 30, 40, 10, 30]
print(first_last_number_same(_list1))

