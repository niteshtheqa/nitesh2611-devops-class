# Question 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def print_patterns_1():
    for row in range(1, 5):
        for col in range(row):
            print(row, end=" ")
        print('')


print_patterns_1()
