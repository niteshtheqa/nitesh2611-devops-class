# Question 15: Write a function called exponent(base, exp) that
# returns an int value of base raises to the power of exp.
class question_15:

    def power_of_exp(self, base, exp):
        result = 1
        while exp > 0:
            result = result * base
            exp -= 1
        print(base, "raises to the power of ", exp, "is : ", result)


obj = question_15()
base = int(input("Enter base:   "))
exp = int(input("Enter exp: "))
obj.power_of_exp(base, exp)
