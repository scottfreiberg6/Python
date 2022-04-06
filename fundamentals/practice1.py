students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary
def iterateDictionary (some_list):
    for element in some_list:
        print(element)
        newStr = " "
        for key, val in element.items():
        # print (f"{key} -{val}")
            newStr += f"{key}-{val},"
        print(newStr)

        iterateDictionary(students)