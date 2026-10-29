# # Lets get started

# x = []

# y = [1,2,3,4,5]

# z = [1,"Hello","Two",67,True]


# print(x)
# print(y)
# print(z)

# x1 = [True, False, 22,11, "Hey"]
# x = x1

# print(x)
# print(x1)

# # Create an empty list called shopping. 
# # Then create another list called prices containing five numbers of your choice. Print both lists.

# shopping = []
# prices = [1,2,3,4,5]

# # Create a list called student that contains
# # a student's name (string), age (integer), height (float), and whether they are enrolled (Boolean). 
# # Print the list.

# class Student:
#     def __init__(self,name,age,height,is_enrolled):
#         self.name = name 
#         self.age = age
#         self.height = height
#         self.is_enrolled = is_enrolled


# student1 = Student("Joseph",11,180,False)
# student2 = Student("Jose",100,190,True)
# student3 = Student("Gusepphie",11,180,False)
# student4 = Student("Gullati",100,190,True)
# students = [student1, student2, student3, student4]
# for student in students:
#     if student.is_enrolled == True:
#         print(student.name)

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota","Cool",2007)
car2 = Car("Honda","Camry",2017)
car3 = Car("Mazda","3",2001)
car4 = Car("Mercedes","67",2026)

cars = [car1,car2,car3,car4]

for car in cars:
    if car.year < 2020:
        print(car.make)