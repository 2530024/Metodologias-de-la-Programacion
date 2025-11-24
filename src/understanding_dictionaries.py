#Simple dictionary
alien_0 = {'color': 'green', 'points': 5}

#The simpliest dictionary
alien_1 = {'color': 'yellow'}

#Accessing values in a dictionary
print(alien_0['color'])
print(alien_1['color'])

#Empty
alien_2 = {}

#Modifying values in a dictionary
alien_2 = {'color': 'red'}
alien_2['color'] = 'blue'

#Adding new key values pairs
alien_2['x_position'] = 0
alien_2['y_position'] = 25

##Dictionaty to store similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

#Looping throgh all key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for key in favorite_languages.keys():
    print(key.title())

for value in favorite_languages.values():
    print(value.title)

#Nesting dictionaries

##Listas de diccionarios
##Listas en diccionarios
##Diccionarios en diccionarios
