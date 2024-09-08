'''
Decision making statements --> Conditional statements

if
elif
else
netsted if
'''

'''
syntax:
if condition:
    statements
else 
    statements
'''

#if True:
#    print("I'm if")
#elif True:
#    print("I'm elif")
#else:
#    print("I'm else")
    
'''Nested if'''
 
#if False:
#    print("I'm outer if")
#    if False:
#        print("I'm inner if")
#    else:
#        print("I'm inner else")
#else:
#    print("I'm outer else")
    
'''Real program'''

#age = 18
#if age>18:
#    print("You can vote")
#elif age==18:
#    print("You are eligibile for voting")
#else:
#    print("Wait")
    
#age = 18
#if age>18 or age ==18:
#    print("You can vote")
#else:
#    print("Wait")

'''Looping Statements
for
while

'''
#for i in range(1,10,2):
#    print(i)
    
#a = [1,2,3,4,5,6,7,88,33,34,11]
#for i in a:
#    print(i)    

#a = 'Sujith'
#for i in a:
#   print(i)
   
#while True:
#    print("Hello!!") 

#sn = 10
#while sn<24:
#    print("HI",sn)
#    sn+=1
    
'''
Diff b/w for & while
Range is used in for, But not in while
'''
for i in range(0,10):
    for j in range(0,100):
        print(i+j)
        