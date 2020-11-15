"""
Question 11: Write a code to extract each digit from an integer,
in the reverse order"""


class Test1:

    def extract_digit_in_reverse_order(self, number):
        originalNumber = number
        reverse_number = 0
        while number > 0:
            remainder = number % 10
            reverse_number = (reverse_number * 10) + remainder
            number = number // 10
        return reverse_number


obj = Test1()
print("Reversed Number : ", obj.extract_digit_in_reverse_order(7536))
