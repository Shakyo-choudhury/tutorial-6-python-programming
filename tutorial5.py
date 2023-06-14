myInt = 143 #integer 
myFloat = 1.43 #float
myResult = myInt + myFloat #gives the sum of myint and myfloat
print("Value of myResult:",myResult) #myresult datatype
print("datatype of myResult:",type(myResult))
print("datatype of myInt:",type(myInt))
print("datatype of myFloat:",type(myFloat))



'''
str() -> converts to string datatype
bool() -> converts to boolean datatype
complex() -> converts to complex datatype
float() -> converts to float datatype
int() -> converts to integer datatype
'''
# syntax -> (required_datatype)(expression)
print(int(10+3j)) #complex - throws an error
print(int("10.5")) #string - throws an error
print(int("10")) #string
print(int(False)) #boolean
print(int(123.654)) #float


print(float("10.5"))
print(float("10"))
print(float(False))
print(float(True))
print(float(10))
# after using float function we get a decimal point after the number


# # complex function
print(complex(10))
print(complex(10.5))
print(complex(True))
print(complex(False))
print(complex("10"))
print(complex("10.5"))
#print(complex("ten")) #error



#form 2 
print(complex(10,-2)) - 10 -2j
print(complex(True, False)) 1+0j


# # boolean type conversion
print(bool("")) #gives false
print(bool("Apple"))
print(bool(0+0j)) #gives false
print(bool(0+15j))
print(bool(10+6j))
print(bool(0.13332))
print(bool(10))
print(bool(1))
print(bool(0)) #gives false

# string type conversion
print(str(10+5j))
print(str(False))
print(str(True))
print(str(10.5))
print(str(456))
print(str(10))
