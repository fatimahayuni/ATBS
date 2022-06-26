def spam():
    global eggs
    eggs = 'spam' # this is global variable cos above it has been defined as 'global eggs'

def bacon():
    eggs = 'bacon' # this is local variable cos it is within a function

def hams():
    print(eggs) # this is global. egg is the global. why? it is not even a variable. it is within a functionand no declaration.

eggs = 42 # this is global variable
spam()
print(eggs)
