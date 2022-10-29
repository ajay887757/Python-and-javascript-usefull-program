class calc:
    def __init__(self,a,b):
        self.a = a#self is use for all to use in another function
        self.b = b #ab is noraml varible we change self a.b to use in all functions
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b


def tryExcept():
    try:
        a = int(input('Enter First number : '))
        b = int(input('Enter Second number : '))        
        obj=calc(a,b)
        x = ('1. Add \n2. Sub \n3. Multiply \n4. Divide') 
        print(x)
        choice = int(input('Please select one of the following : ')) 

        if choice == 1:
            print("Result: ",obj.add())
        elif choice == 2:
            print("Result: ",obj.sub())
        elif choice == 3:
            print("Result: ",obj.multiply())    
        elif choice == 4:
            print("Result: ",obj.divide())
        elif choice == 0:
            print('Again try one of the following')
    except Exception as e :
                print ("Invalid number\n"+str(e))


tryExcept()