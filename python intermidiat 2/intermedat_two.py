# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]


# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15 
# print(x)


# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]['last_name'] = 'Bryant'
# print (students)
# # In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)
# # Change the value 20 in z to 30
# z[0] ['y'] = 30
# print(z)
# print("_" *30)


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
     ]
def  iterateDictionary(students):
    for student in students:
 
        print(f"first name - {student['first_name']} , last name - {student['last_name']}" ) 
iterateDictionary(students)

#another way : 

# def  iterateDictionary(students):
#    for student in students:
#     for  key,value in students:
#      print(f"{key} - {value}", end="," ) 
# iterateDictionary(students)

def  iterateDictionary2(key_name,students):
    for student  in students:
         print(student[key_name]) 

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students )


