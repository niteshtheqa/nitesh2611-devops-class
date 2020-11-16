# Question 13: Print multiplication table form 1 to 10

for row in range(1,11):
    for col in range(1,11):
        print(row * col,end=" ")
    print("\t\t")