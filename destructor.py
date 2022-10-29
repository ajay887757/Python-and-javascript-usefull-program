class test():
    def __init__(self) :
        print("Hello This is from constructor")


    def __del__(self):
        print("Destructor Execution ")

    @property   # property method is use for when you are converting method to property that time its useable you can call that method like that t2.m1
    def m1(self):
        print("Hello Boys")


t1=test()
t1=None
t2=test()

t2.m1
print("End of the Programm")