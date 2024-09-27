'''
list
'''

# v =[]
# print(type(v))

#v1 = [1,5,6,75,'sujith']
# print(v1) --> Printing the list
# print(v1[3]) --> 75
# print(v1[-1]) --> For printing the last element --> Known as negative indexing

# print(v1[0:4:2]) --> slicing the list -->[start:stop:skip] --> [s:s:s]

'''
append - To the element at the last in a list
extend - To add the bulk data
count - To count the particular element in the list
pop - To remove the element based on the index
insert - To add an element at particular location
remove - To remove the particular element in the list
index - Will let you know the index of a particular element in the list
'''

v = [1,45,72,1,36,'sujith']
# v.append("Python") --> Add at the last in the list.
# v.extend([5,8,32,44,68,'Sam']) --> When you want to add the bulk data.

# print(v.count(1)) --> To know the count of particular element in the list
# v.remove(45) --> To remove the particular element in the list
# v.pop(1) --> Remove the element based on index 
# print(v.index(45)) --> To find the index of the element

#for i in [1,45,72,1,36,'sujith'] : --> To loop every element in the list
#    print(i)
    
v.insert(0,"xyz")
print(v)    
