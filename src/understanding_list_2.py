#SLICING
players = ["cr7", "messi", "Travis Kelce", "chicha", "corona"]
print(players[0:3])
#Un slice es trabajar con un grupo especifico de elementos de una lista
print(players[1:4])#['messi', 'Travis', 'chicha']
print(players[:4])#['cr7', 'messi', 'Travis', 'chicha']
print(players[2:]) #['Travis', 'chicha', 'corona']
print(players[-3:])#['Travis', 'chicha', 'corona']
print(players[-3:-1])#['Travis', 'chicha']
print(players[4:2])#[]lista vacia

# Slicing en for
players = ["axel", "ignacio", "Travis Kelce", "chicha", "corona", "jorge"]
first_three_players = players[0:3]
print("First three players", first_three_players)

print("Aqui vienen los tres mejores del salon: ")
for player in players[0:3]:
    print(player.title())

#Copia de lista
my_food = ['pizza', 'gorditas de jaumave', 'machacado']
# copy_of_food = my_food  # Manera incorrecta de copiar una lista
copy_of_food_1 = my_food[:]
copy_of_food_2 = my_food.copy()
copy_of_food_3 = list(my_food)

#Moodificando elementos
cars = ['bwm', 'porch', 'masda', 'totoya', 'ford']
cars[0]="bmw"
cars[1]="porshe"
cars[2]="mazda"
cars[3]="toyota"