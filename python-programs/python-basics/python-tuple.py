#   A tuple is a collection which is ordered and unchangeable.
#   In Python tuples are written with round brackets.

class tuples:


    def access_items_from_tuple(thistuple):
        print("Print tuple: ",thistuple)
        print("Print item[0]:",thistuple[0])
        print("Print item[1]:", thistuple[1])
        print("item[-1]",thistuple[-1])

    def range_indexing(thistuple):
        print(thistuple[1:])

    def change_item_value(thistuple):
        print(""""'tuple' object does not support item assignment.In order to execute tis we have
        to convert tuple to list and then use assignment operator to set value""")
        print("Original Tuple: ",thistuple)
        list1 = list(thistuple)
        list1[2] = 'Pineapple'
        print("Print Tuple after modified the tuple :  ",tuple(list1))

    def loop_through_tuple(thistuple):
        for x in thistuple:
            print("Item:",x)
    def add_item_to_tuple(thistuple):
        thislist = list(thistuple)
        thislist.append('Custard')
        print("Tuple after modidification: ",tuple(thislist))

    def join_tuple():
        print("Join tuple.....")
        tuple1 = ("a", "b", "c")
        tuple2 = (1, 2, 3)
        print("Tuple1:",tuple1)
        print("Tuple2:", tuple2)
        tuple3 = tuple1 + tuple2
        print(tuple3)




thistuple = ("apple", "banana", "cherry")
tuples.access_items_from_tuple(thistuple)
tuples.range_indexing(thistuple)
tuples.change_item_value(thistuple)
tuples.loop_through_tuple(thistuple)
tuples.add_item_to_tuple(thistuple)
tuples.join_tuple()