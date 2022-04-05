
x = [ [5,2,3], [10,8,9],5 ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20}]
test=[5,2,3]

x[1][0]=15
print(x)
print(x[0])
print(x[0][1])
print(students)
print(students[0])
print(students[0]["last_name"])
students[0]["last_name"]="Bryant"
sports_directory['soccer'][0]='Andres'
print(sports_directory['soccer'][0])
print(students)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary
def iterateDictionary (some_list):
    for i in range(0, len(students), 1):
        print(f"{i} + {students[i]}")
iterateDictionary(students)

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
def iterateDictionary2 (key_name,some_list ):
    for i in range(0, len(students), 1):
        if (key_name == "first_name"):
            print(some_list[i]["first_name"])
        else:
            print(some_list[i]["last_name"])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# def printInfo(key_name,some_dict):
#     for i in range(0,len(dojo),1):
#         if(some_dict=='locations'):
#             print(some_dict,'location')
#         else:
#             print(some_dict,'instructors')
# printInfo('locations', dojo)
# printInfo('instructors', dojo)
def printInfo(some_dict):
    for key,val in some_dict.items():
        print(f"{len(val)} {key}")
        for v in val:
            print(v)
printInfo(dojo)