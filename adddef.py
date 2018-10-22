def addition(a, b):
    add = a + b
    return add

xs = input('Pirmais skaitlis: ')
try:
    x = int(xs)
except:
    try:
        x = float(xs)
    except:
        print('Invalid character')
        quit("Lol")
ys = input('Otrais skaitlis: ')
y = float(ys)
xy = addition(x, y)
print(xy)
##
##big = max('Hello world')
##sml = min('Hello world')
##print(big)
##print(sml)
##
##print(type(xs))
##xf = int(xs)
##print(type(xf))
##
##def printtext():
##    print("And on that one fateful day, The Shadow cast it's power unto the world")
##    print("Not all was lost though.")
##    print('The very next day, Light came and scared The Shadow away.')
##
##print(printtext())
##
##def greet(lang):
##    if lang == 'es':
##        return 'Hola'
##    elif lang == 'fr':
##        return 'Bonjour'
##    else:
##        return 'Hello'
##
##print(greet('en'),'Glenn')
##print(greet('es'),'Sally')
##print(greet('fr'),'Micheal')
