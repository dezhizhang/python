

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"姓名:{self.name} 年龄:{self.age}"

stu = Student("tom",22)
print(stu)


