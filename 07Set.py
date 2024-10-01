#s={}
#print(type(s))  --> By default it is considered as dictionary, But when you place elements in the curly brakets then it will consider as dict or set


#s = {1,3124,3}
#print(type(s))


s={2,42,5,25,2,5,2,55,1,0,4}

'''
Methods of Set
add --> adding an element
update --> Adding bulk data
pop --> Deletes an element randomly
remove --> remove particular element
'''

#print(s) --> Set doesn't allow duplicates --> Set is unordered where the order in the input is not same when we get the output.

#s.add(123)
#s.update({1,2,4,35,5})
#s.pop()
#s.remove(25)
#print(s) 

'''
Operations of Set
Union --> all without duplicates
intersection --> common elements
difference
isusbset
issuperset
'''

#set1={1,2,3,4}
#set2={4,5,6}
# print(set1.union(set2)) --> In union, we will get total data without duplicates
# print(set1.intersection(set2)) --> Only shows the common element from both sets
# print(set1.difference(set2)) --> Shows only elements in set1 which are not same as set2.

set1={1,2,3,4,5,6}
set2={1,2,3}

# print(set1.issuperset(set2)) --> All elements in set1 should also be present in set2.
# print(set1.issubset(set2)) -->

for i in {1,2,3,4}:
    print(i)