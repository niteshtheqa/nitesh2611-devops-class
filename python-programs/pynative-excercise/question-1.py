#Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, 
#then return their sum


def multiplication_or_sum(num1 , num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number:    '))

print("\n")
result = multiplication_or_sum(num1,num2)
print('Result:  ',result)

