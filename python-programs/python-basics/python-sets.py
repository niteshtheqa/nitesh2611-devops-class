# A set is a collection which is unordered and unindexed.
# In Python, sets are written with curly brackets.

class sets:
    def access_items(thisset):
        print("Set: ",thisset)
        for item in thisset:
            print(item)

    def check_item_is_present(thisset):
        if "apple" in thisset:
            print("yes, 'apple' is present")

    def add_item_set(thisset):
        print("Original Set:",thisset)
        thisset.add("pineapple")
        print("Modified Set:    ",thisset)

    def add_multiple_items_to_set(thisset):
        print("Original Set:", thisset)
        thisset.update(["1","2","3","4"])
        print("Modified Set:    ", thisset)


    def join_two_set():
        set1 = {"a", "b", "c"}
        set2 = {1, 2, 3}

        set3 = set1.union(set2)
        print("Joined set:   ",set3)

thisset = {"apple", "banana", "cherry"}
sets.access_items(thisset)
sets.check_item_is_present(thisset)
sets.add_item_set(thisset)
sets.add_multiple_items_to_set(thisset)
sets.join_two_set()