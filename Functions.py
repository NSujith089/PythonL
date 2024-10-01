'''
function - A block of code
'''

#def func(): # function definition
#    print("This is a function") # function body
# func () # function call --> Without function call we don't get the outout

#def func(a) --> Single Parameter
#def func(a,b,c) --> Multi Parameters

#func(1,2,3) --> Arguments

#def func(a,b,c):
#    print("This is Function",a,b,c)
#func(1,2,3)

#Keyword Arguments


#orbitory Arguments --> if we use star (*), Then it is know an orbitaty arguments

#def func(*a):
#    print("This is function",a) # Now we will get the output in tuple format as we are using single star (*)
#func(1,2,3)

#def func(**a):
#    print("This is function",a) # Now we will get the output in dictionary format as we are using two star (**)
#func(a=1,b=2)

# Nested Function

#def outer():
#    print("Outer Function")
#    def inner():
#        print("Inner Function")
#    inner()
#outer()

# About Import Keyword

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)