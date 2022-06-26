# LOCAL SCOPES CANNOT USE VARIABLES IN OTHER LOCAL SCOPES
# def(spam is a definition of the function.
# but the actual calling of the spam() is at the end of the code.m
# so when spam() appears, Python will read the def spam() local variable
# in which there are eggs = 99.
#but in the same local function, a function bacon() is created and thus
# this will create a second local function which is def bacon() (line 15)
# so when python sees bacon(), it will find a corresponding local variable to that
# and find def bacon() function.
# python continues evaluating and looking for print() now which it is the final evaluation.
# so it goes back up the top of the code and finds print(eggs).
# it will print 99 not 10 bcos when it ran through bacon() and back up to the top,
# it has destroyed the local scope for def bacon()
# summary: local scopes cannot use variables in other local scopes


def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
