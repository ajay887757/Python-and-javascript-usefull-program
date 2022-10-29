# import re

# class check:
    
#     def validate_pincode(self,pincode):
#         self.pincode=pincode
#         pattern = re.compil = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$";
#         if re.fullmatch(pattern, self.pincode):
#             return f"'{user_pincode}' is a valid pincode!"
#         elif len(self.pincode)==0:
#             return "Field required"
#         else:
#             return f"'{user_pincode}' is an invalid pincode!"
# user_pincode = str(input("Enter the pincode: "))
# user_pincode = user_pincode.strip()
# object = check()
# object.validate_pincode(user_pincode)

# result = re.sub(r'\s+', '', user_pincode)
# print(result)
# print(object.validate_pincode(user_pincode))



import re
class check:
      def __init__(self,user_pincode,address):
        self.user_pincode = user_pincode
        self.address = address
      def validate_pincode(self):
       
            pattern = re.compile = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$";
            if re.fullmatch(pattern, self.user_pincode):
                return f"'{user_pincode}' is a valid pincode!"
            elif len(self.user_pincode) == 0:
                return "Field required"
            else:
                return f"'{user_pincode}' is an invalid pincode!"
user_pincode = str(input("Enter the pincode: "))
address=input("Enter Address: ")
user_pincode = user_pincode.strip()
object = check(user_pincode,address)

result = re.sub(r'\s+', '', user_pincode)
print(result)
print(object.validate_pincode())