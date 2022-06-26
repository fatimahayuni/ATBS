while True:
    print('What is your name?')
    name = input()
    if name == '':
        continue
    print('Hello. How old are you?')
    age = input()
    if age == '':
        break
    print('Thanks for filling in the form')
