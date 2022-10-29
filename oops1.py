class First():
    def __init__(self,name):
        self.name=name
    
    def m1(self):
        print("name from 1",self.name)

class Second():

    def __init__(self,rollno):
        self.rollno=rollno

    def m3(self):
        print(self.rollno)


class NewClass(First):

    def __init__(self, name,roll):
        super().__init__(name)
        self.roll=roll

    def InheritedMethod(self):
        print("Hello World")
        self.m1()
        # pass

    def m1(self):
        super().m1()
        print(self.roll)

# First("Ajay")
# Second(5)

obj=NewClass("Hello Ajay",33)
obj.InheritedMethod()
obj.m1()