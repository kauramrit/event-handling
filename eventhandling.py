#Q.1- Name and handle the exception occured in the following program: 

Name:ZeroDivisionError

a=3
try:
    if a<4:
        print(a=a/(a-3))
except ZeroDivisionError as msg:
    print(msg)


#Q.2- Name and handle the exception occurred in the following program: 

Name:IndexError

try:
    l=[1,2,3]
    print(l[3])
except IndexError as msg:
    print(msg)


#Q.3- What will be the output of the following code:

    # Program to depict Raising Exception
     
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not

OUTPUT:
    An Exception
    NameError: Hi there
    
#Q.4- What will be the output of the following code: 

     # Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    
    # Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
    
OUTPUT:
-5.0
a/b result in 0


#Q.5- Write a program to show and handle following exceptions: 
#1. Import Error 
#2. Value Error 
#3. Index Error

print("PROGRAM FOR ImportError:")
'''the ImportError is raised when an import statement has trouble \
    successfully importing the specified module.'''
import sys
try:
    from exception import myexception
except Exception as a:
    print(a)
print()

print("PROGRAM FOR ValueError:")
'''In Python , a value is the information that is stored within\
    a certain object. To encounter a ValueError in Python means that\
    is a problem with the content of the object you tried to assign\
    the value to'''

try:
    x=int(input("enter a number"))
    print(x)
except ValueError as message:
    print(message)
print()

print("PROGRAM FOR IndexError:")
'''It is raised whenever attempting to access an \
    index that is outside the bounds of a list'''
try:
    l=[1,2,3]
    print(l[3])
except IndexError as message:
    print(message)
print()



