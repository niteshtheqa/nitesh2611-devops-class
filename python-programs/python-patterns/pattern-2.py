# Question 14: Print downward Half-Pyramid Pattern with Star (asterisk)


# num = 0
class Patterns:

    # for row in range(6,0,-1):
    #     #num +=1
    #     i = 0
    #     for col in range(0,row+1):
    #         print(i, end=" ")
    #         i += 1
    #         #print(row,end=" ")
    #         #print("*", end=" ")
    #         #print(num, end=" ")
    #         #print("5", end=" ")
    #
    #     print(" ")

    #     * * * * *
    #     * * * *
    #     * * *
    #     * *
    #     *
    def pattern1(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 1:")

        for row in range(6, 0, -1):
            for col in range(1, row + 1):
                print("*", end=" ")
            print(" ")

    # 1 1 1 1 1
    # 2 2 2 2
    # 3 3 3
    # 4 4
    # 5

    def pattern2(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 2:")
        num = 0
        for row in range(5, 0, -1):
            num += 1
            for col in range(1, row + 1):
                print(num, end=" ")
            print(" ")

    # 5 5 5 5 5
    # 5 5 5 5
    # 5 5 5
    # 5 5
    # 5
    def pattern3(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 3:")
        num = 5
        for row in range(5, 0, -1):
            for col in range(1, row + 1):
                print(num, end=" ")
            print(" ")

    # 0 1 2 3 4 5
    # 0 1 2 3 4
    # 0 1 2 3
    # 0 1 2
    # 0 1

    def pattern4(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 4: ")
        for row in range(5, 0, -1):
            num = 0
            for col in range(0, row + 1):
                print(num, end=" ")
                num += 1
            print(" ")

    # 1
    # 2 1
    # 3 2 1
    # 4 3 2 1
    # 5 4 3 2 1

    def pattern5(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 5:  ")
        for row in range(1, 6):
            num = row
            for col in range(1, row + 1):
                print(num, end=" ")
                num -= 1
            print(" ")

    #   1
    #   2    1
    #   4    2    1
    #   8    4    2    1
    #  16    8    4    2    1
    #  32   16    8    4    2    1
    #  64   32   16    8    4    2    1
    # 128   64   32   16    8    4    2    1

    def pattern6(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 6:  ")
        for row in range(1, 10):
            for col in range(row - 1, -1, -1):
                print(format(2 ** col, "4d"), end=" ")

            print(" ")

    def pattern7(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 7:  ")
        for row in range(1, 10):
            for col in range(1, row, 1):
                print(format(2 ** col, "4d"), end=" ")
            for col in range(row - 1, -1, -1):
                print(format(2 ** col, "4d"), end=" ")

            print(" ")

    # 1
    # 2 3 4
    # 5 6 7 8 9
    def pattern8(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 8:  ")
        num = 0
        for row in range(1, 6, 2):
            for col in range(1, row + 1):
                num += 1
                print(num, end=" ")
            print(" ")

    # 1
    # 2 3
    # 4 5 6
    # 7 8 9 10

    def pattern9(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 9:  ")
        num = 0
        for row in range(1, 5):
            for col in range(1, row + 1):
                num += 1
                print(num, end=" ")
            print(" ")

    def pattern10(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 10:  ")
        next = 2
        prev = 1
        num = next
        for row in range(2, 6):
            for col in range(prev, next):
                num -= 1
                print(num, end=" ")
            print(" ")
            prev = next
            next += row
            num = next

    # 10
    # 10 8
    # 10 8 6
    # 10 8 6 4
    # 10 8 6 4 2

    def pattern11(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 11:   ")
        rows = 5
        for row in range(1, 7):
            num = rows * 2
            for col in range(1, row):
                print(num, end=" ")
                num -= 2
            print(" ")

    def pattern12(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 12:   ")
        num = 1
        for row in range(1, 6):
            for col in range(1, row + 1):
                print(col, end=" ")
            for col in range(row - 1, 0, -1):
                print(col, end=" ")

            print(" ")

    # 5 4 3 2 1
    # 4 3 2 1
    # 3 2 1
    # 2 1
    # 1

    def pattern13(self):
        print("\n")
        print("\n")
        print("\n")
        print("Pattern 13:   ")
        for row in range(5, 0, -1):
            for col in range(row, 0, -1):
                print(col, end=" ")
            print(" ")

    def pattern14(self):
        print("\n")
        print("\n")
        print("\n")
        prev = 0
        next = 1
        print("Pattern 14:   ")
        for row in range(0, 6):
            for column in range(0, row + 1):
                print( row * column , end=" ")
            print(" ")


pattern = Patterns()
pattern.pattern1()
pattern.pattern2()
pattern.pattern3()
pattern.pattern4()
pattern.pattern5()
pattern.pattern6()
pattern.pattern7()
pattern.pattern8()
pattern.pattern9()
pattern.pattern10()
pattern.pattern11()
pattern.pattern12()
pattern.pattern13()
pattern.pattern14()
