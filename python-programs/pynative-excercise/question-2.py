# Question 2: Given a range of first 10 numbers, Iterate from start number to the end number
# and print the sum of the current number and previous number

def print_sum_of_current_num_with_previous_num(num):
    previousNumber = 0
    for i in range(num):
        previousNumber + i
        print('Current Number:  {} ,Previous Number :{},Addition is: {}'.format(
            i, previousNumber, i + previousNumber))
        previousNumber = i


number = int(input('Enter number :  '))
print_sum_of_current_num_with_previous_num(number)
