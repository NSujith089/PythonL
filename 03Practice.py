"""
Jumping Statements:
1.Pass --> Ignore (If the statements are not yet finalized)
2.Break --> Terminate (if the condition is true)
3.Continue --> Skip (Current iteration)
"""

#if True:
#    pass  #Using we can avoid error and add the statements later.#

#for i in "Pythonlife":
#    if i == 'l':
#        break
#    print(i)

for i in "Pythonlife":
    if i == 'y':
        continue
    print(i)