# class Student(object):
#     name = None
#     age = None
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age
#
#
#
# stu1 = Student("jack",33)
# stu2 = Student("jack",33)
#
# print(stu2 == stu1)

class Student:
    name = None
    age = None

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("tom",22)
stu2 = Student("jack",22)

print(stu2 == stu1)

