#dictionary consists of (key:value) pair --> [k:v]
#Keys are unique.
#Values are duplicates sometimes.
#No indexing and slicing in dictionary

#d={}
#print(type(d))

#d = {1:'abc',22: 'sn','sujith':10}
#print(d)
#print(d[22])

'''
Dictionary Methonds:
 get 
 update
 values
 key
 item
'''

#d = {1:'abc',22: 'sn','sujith':10}
#print(d.get(1)) --> It will take key inside get.
#print(d.keys()) --> Will print all keys from the dictionary.
#print(d.values()) --> Will print all the values from the dictionary.
#print(d.items()) --> Will print all the items from the dictionary.
#d.update({1111:2222})
#print(d)

#for i in {1:'abc',22: 'sn','sujith':10} :
#    print(i) --> Prints only keys from the dictionary
    
    
#for i in {1:'abc',22: 'sn','sujith':10}.values() :
#    print(i)
 
for i,j in {1:'abc',22: 'sn','sujith':10}.items() :
    print(i,j)