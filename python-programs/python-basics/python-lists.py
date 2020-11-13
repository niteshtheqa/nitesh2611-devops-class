"""
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
"""



class lists:

    def access_items(list1):
        print(list1[0])

    def negative_indexing(list1):
        print(list1[-2])


    def range_indexing(list1):
        print(list1[2:5])

    def change_item_value(list1):
        print("Original List: ",list1)
        list1[3] = 'Pineapple'
        print("List after modified the list :  ",list1)

    def creating_newlist_using_chars_without_comprehension():
        newList = []
        fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
        for x in fruits:
            if 'e' in x:
                newList.append(x)
        print("New List without comprehension:  ",newList)

    def creating_newlist_using_chars_with_comprehension():
        fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
        newList = [x for x in fruits if 'a' in x]

        print("new List with comprehension:  ",newList)

    def check_if_item_exists_list(list1):
        if 'banana' in list1:
            print("Yes, 'banana' is present in list")
        else:
            print("'banana' , is not present in lists")

    def add_new_item_to_list(list1):
        list1.append('Pickle')
        print("new list after item appended:  ",list1)

    def insert_item_at_specified_index(list1):
        list1.insert(2,'Avagrado')
        print("'Avagrado' inserted at index 2")
        print(list1)
    def pop_item(list1):
        print("Original list:",list1)
        list1.pop(1)
        print("New list after item poped out: ",list1)
    def delete_item_from_specified_index(list1):
        print("Original List:",list1)
        del list1[0]
        print("List after item deleted:",list1)

    def reverse_list(list1):
        print("Original List:", list1)
        list1.reverse()
        print("Reversed List:   ",list1)

thelist =[10,20,10,50,30,90]
thislist =  ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
lists.access_items(thelist)
lists.negative_indexing(thislist)
lists.range_indexing(thelist)
lists.change_item_value(thelist)
lists.creating_newlist_using_chars_without_comprehension()
lists.creating_newlist_using_chars_with_comprehension()
lists.check_if_item_exists_list(thislist)
lists.add_new_item_to_list(thislist)
lists.insert_item_at_specified_index(thislist)
lists.pop_item(thislist)
lists.delete_item_from_specified_index(thislist)
lists.reverse_list(thislist)