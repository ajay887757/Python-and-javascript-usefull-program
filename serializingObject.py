import jsonpickle


class test():
    x=10
    def __init__(self,name):
        self.x=test.x
        self.name=name

    def display(self):
        print("Name {}".format(self.name))

t=test("Ajay")
# dict_data=t.__dict__
# print(dict_data)
# t.display()

#serializing to the json

jsonString=jsonpickle.encode(t)
print(jsonString)

#deserialized json to orignal form

dictData=jsonpickle.decode(jsonString)
print("dictData",dictData)
dictData.display() 
print("getting class name",dictData.__class__.__name__)

