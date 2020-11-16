"""Question 10: Given a two list of numbers create a new list such that new list
should contain only odd numbers from the first list and even numbers from the
second list"""


class question_9:

    def merge_lists(self):
        firstList = [10, 20, 23, 11, 17]
        secondList = [13, 43, 24, 36, 12]
        newList = []
        for item in firstList:
            if item % 2 == 0:
                newList.append(item)
        for item in secondList:
            if item % 2 != 0:
                newList.append(item)
        print("Newly created List: ", newList)


obj = question_9()
obj.merge_lists()
