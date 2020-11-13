# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets,
# and they have keys and values.

class dictionary:


    def access_items(thisdict):
        print(thisdict)
        print("Year with Key:    ",thisdict["year"])
        model = thisdict.get("model")
        print("Model with get():    ",model)

    def change_value(thisdict):
        print("Original Dictionary: ",thisdict)
        thisdict["year"] =2020
        thisdict["brand"] ="MG Hector"
        thisdict["model"] = "Gloster"
        print("Dictionary with updated values: ",thisdict)

    def loop_through_dictionary(thisdict):
        print("Prinitng all keys.....")
        for keys in thisdict:
            print("Key: ",keys)
        print("Prinitng all values.....")
        for keys in thisdict:
            print("Value:",thisdict[keys])
        print("Prinitng all dictionary.....")
        for keys in thisdict:
            print("Key: ",keys,"::","Value:",thisdict[keys])


    def loop_using_values_method(thisdict):
        for x in thisdict.values():
            print(x)

    def loop_using_items_method(thisdict):
        for key,value in thisdict.items():
            print(key," : ",value)

    def check_if_key_exists(thisdict):
        print(thisdict)
        if "year" in thisdict:
            print("yes, present")
    def add_item_to_dict(thisdict):
        thisdict["color"] = "red"
        print("Color added: ",thisdict)
        for x,y in thisdict.items():
            print(x," ==> ",y)






thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


dictionary.access_items(thisdict)
dictionary.change_value(thisdict)
dictionary.loop_through_dictionary(thisdict)
dictionary.loop_using_values_method(thisdict)
dictionary.loop_using_items_method(thisdict)
dictionary.check_if_key_exists(thisdict)
dictionary.add_item_to_dict(thisdict)