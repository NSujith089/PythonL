# Tuple is immutable --> We cannnot add the elements.
#c = ()
#print(type(c)) --> Empty Tuple

#c=(1,24,1,3,14,14,'sujith')
#print(c[-1]) --> Indexing is possible
#print(c[0:4:2]) --> Slicing is also possible --> [s:s:s]

#c=(1,24,1,3,14,14)
#print(min(c)) --> minimum element
#print(max(c)) --> maximum element
#print(sum(c)) --> calculates sum
#print(len(c)) --> Finds the length of tuple


#t1=(1,2,3)
#t2=(4,5,6)
#print(t1+t2) --> Concatenate two tuples


#c=(1,24,1,3,14,14)
#print(c*11) --> 11 times repeatation

#for i in c : --> we can do Iteration as well 
#    print(i)

#print(1 in c) --> This is membership operation if the particular element is in the list, then it is known as TRUE else FALSE.
#print(11 not in c) --> TRUE --> Membership Operator (in or not in)

#t1=(1,2,3)
#t2=(4,5,6)
#print(t1 is t2) --> Shows as false as elements in t1 are not similar to elements in t2
#print(t1 is not t2) --> Shows as True as elements in t1 are not similar to elements in t2 as expected.

#t1=(1,2,3)
#t2=(1,2,3)
#print(t1 is t2) --> Shows as true because both elements are similar in both t1 and t2. --> identity
