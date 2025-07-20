

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __lt__(self,other):
#         return self.age < other.age
#
#
#
# stu1 = Student("tom",22)
# stu2 = Student("jack",33)
#
# print(stu1 < stu2)

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __lt__(self,other):
        return self.age < other.age


stu1 = Student("tom",22)
stu2 = Student("jack",33)

print(stu1 < stu2)

