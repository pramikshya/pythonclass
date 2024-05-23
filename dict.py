#Dictionary: it stores data in the basis of key and value
#key always string "name"


student={
    "name":"sudan",
    "surname":"bhandari",
    "age":27,
    "phone":[98062, 98449]
}
# print(type(student))
# print(student['name'])
# print(student['phone'][0])

# print(a[0]+a[1])

# print(str(student["phone"][1])+str(student["phone"][0]))
# print(student.keys())

# #Dict Method...
# print(student['testing'1])

# student['testing']='hello world'
# print(student)
# student['phone']='98'
# print(student)


print(len(student))

student={
    "name":"sudan",
    "surname":"bhandari",
    "age":27,
    "phone":[98062, 98449]
}
del student['surname']
print(student)

data = [
    {
        'student':'pranav',
        'teacher':'sudan'
    },
    {
        'student':'pranav',
        'teacher':'sudan'
    }
]

print(f'(student is {data[0]['student']} and teacher {data[0]['teacher']}' )

person ={
    'name':'aditye',
    'address':'banepa',
    'phone':{
        'service_provider':'ntc',
        'number':'98'
    }
}

print(person['phone']['service_provider'])