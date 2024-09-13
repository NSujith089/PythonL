'''
Collection of Characters
'''

# b='Pythonlife' # This is not work in for single quotes --> 'Pyhtonlife's' (Wrong)
# a="Pyhtonlife" # Then We can use double quotes --> "Pythonlife's" (Correct)
# c='''Pyhton
# life''' # When we write multiple lines.
# print(typr(a),type(b),type(c))

'''
String Methods:-

lower
upper
endswith
startwith
replace
find
index
count
remove prefix
remove suffix
split
strip --> Trim
rstirp
lstrip

'''

#python = "please subcribe"
#print(python.upper())

#python = "PLEASE SUBCRIBE"
#print(python.lower())

#python = "python language"
#print(python.endswith("language"))
#print(python.endswith("")) # Don't understand why it is true
#print(python.endswith("l"))
#print(python.endswith("e"))

#python = "python language"
#print(python.startswith("python"))
#print(python.startswith("")) # Don't understand why it is true
#print(python.startswith("p"))
#print(python.startswith("y"))

#python = "python language"
#print(python.replace("language","programming")) #--> replace(old,new)

#python = "python language"
#print(python.index("python")) --> 0
#print(python.index("kiran")) --> Error
#print(python.find("python")) --> 0
#print(python.find("kiran")) --> -1

#print(python.count("p")) --> count of letter
#print(python.count("g")) 
#print(python.count("")) --> cound of whole word

#print(python.removeprefix("python")) --> removes front word
#print(python.removesuffix("language")) --> removes back word
#print(python.removesuffix("python")) --> removes nothing when word doesn't match.

#print(python.split()) --> Converts into list and split.

python = "      python language     "
print(python)
print(len(python))
v=python.strip()
print(len(v))
v=python.lstrip()
print(len(v)) 
v=python.rstrip()
print(len(v)) 

# strip means trim, Can't remove spaces in the middle of 2 words.


