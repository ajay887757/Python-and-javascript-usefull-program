class operatorOverloading():
    def __init__(self,value) -> None:
        self.value=value
        print("Constructor Execution")

    def __add__(self,other):
        # return (self.value-other.value)
        return operatorOverloading(self.value-other.value)

    def __str__(self) :
        return str(self.value)

    def m1(self,*args):
        print(args)


b1=operatorOverloading(100)
b2=operatorOverloading(50)

b1.m1(10,20,30)

print(b1+b2)