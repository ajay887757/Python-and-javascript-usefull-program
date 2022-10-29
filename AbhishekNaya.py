def CheckGoodNumber(num):
    if "7" in str(num):
        return False

    else:
        if num%7==0:
            return True
        else:
            return False

result=CheckGoodNumber(150)
print(result)

