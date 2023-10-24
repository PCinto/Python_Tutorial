class Person:
        def __init__(self, name, age, gender): #init is a constractor method
            self.name = name
            self.age = age
            self.gender = gender

        def derail(self):
            print(self.name, "is studying")

p = Person("Joe", 27, "Male")
p.derail()