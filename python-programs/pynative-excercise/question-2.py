# Question 2: Given a range of first 10 numbers, Iterate from start number to the end number
# and print the sum of the current number and previous number

def print_sum_of_current_num_with_previous_num():
    for i in range(10):
        previousNumber = 0
        print('Current Number:  {} ,Previous Number :{},Addition is: {}'.format(
            i, previousNumber, i + previousNumber))
        previousNumber = previousNumber + i


print_sum_of_current_num_with_previous_num()
