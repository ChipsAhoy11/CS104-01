#Brandon Benanti
#Python Queue Assignment

names = []
for x in range (0,10):
    name = input('Enter a Name: ')
    #names.insert(0, name) 
    names.append(name)
print(names) 

for x in range (0,10):
    print(names.pop(0))
print(names) 
