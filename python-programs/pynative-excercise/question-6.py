# Question 6: Given a list of numbers, Iterate it and
# print only those numbers which are divisible of 5

def is_number_divisible_by_five(number_list):
    for i in number_list:
        if i % 5 == 0:
            print(i)
            

_list1 = [10, 20, 30, 40, 10, 30]
is_number_divisible_by_five(_list1)

