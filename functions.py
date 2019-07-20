def myFunction():
   print("My first function")

myFunction()

# def printName(name):
#    print(f"Hello {name}")

# printName("SK")

def printName(name):
   return f"Hello {name}"

msg = printName("SK")
print(msg)

def increment(number, by=1):
   return number + by

print(increment(2))

def multiply(*numbers): #tuples
   total = 1
   for number in numbers:
       total *= number
   return total

print(multiply(2, 3, 4, 5))

def userDetail(**user): #keyword arguments
    print(user)

userDetail(id = 1, name = "SK", IP = "192.168.0.3")
