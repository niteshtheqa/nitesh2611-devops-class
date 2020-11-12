class lists:

    def access_items(list1):
        print(list1[0])

    def negative_indexing(list1):
        print(list1[-2])


    def range_indexing(list1):
        print(list1[2:5])

    def change_item_value(list1):
        list1[3] = 'Pineapple'
        print(list1)
thelist =[10,20,10,50,30,90]
thislist =  ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
lists.access_items(thelist)
lists.negative_indexing(thislist)
lists.range_indexing(thelist)
lists.change_item_value(thelist)