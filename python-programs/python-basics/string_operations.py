class string_operations:
    def multiline_string():
        a = """Nitesh Wayafalkar"""
        print(a)
    def slicing_of_string(slice_str):
        print("Slicing: ",slice_str[3:6])

    def negative_slicing_of_string(slice_str):
        print("Slicing: ",slice_str[-10:-2])
    def str_strip(string1):
        print(string1.strip())

    def str_split(string1):
         print(string1.split(" "))

    def check_string(string1):
        res =  "Nitesh" in string1
        print(res)

        res =  "Nitesh" not in string1
        print(res)


        print(string1.count('a'))
        print("Center:  ",string1.center(50,'0'))


str1 = 'Nitesh Wayafalkar'
string_operations.multiline_string()
string_operations.slicing_of_string(str1)
string_operations.negative_slicing_of_string(str1)
string_operations.str_strip(str1)
string_operations.str_split(str1)
string_operations.check_string(str1)