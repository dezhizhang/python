
class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel


stu = Student("tom", "22", "15992478448")
print(f"姓名:{stu.name}  年龄:{stu.age} 电话:{stu.tel}")
