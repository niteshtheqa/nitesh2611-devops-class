# Question 9: Reverse a given number and return true if it is the
# same as the original number

def reverseNumber(number):
    originalNumber = number
    rev_number = 0
    while number > 0:
        remainder = number % 10
        rev_number = (rev_number * 10) + remainder
        number = number // 10
    if originalNumber == rev_number:
        return True
    else:
        return False




print(reverseNumber(121))

