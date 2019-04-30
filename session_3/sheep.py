menu = [5, 7, 300 , 90, 24, 50 ,75]

print("Hello , my name is Phuc and there are my sheep sizes :")
print( *menu , sep=", ")

biggest = max(menu)

print("Now my biggest sheep has size",biggest, "let's shear it ")
n = (menu.index(biggest))
menu[n] = "8"
print("After shearing, here is my flock ")
print(*menu,sep=", ")
print("One Month has passed , now here is my flock")
for index , item in enumerate(menu):
    n = int(item)+50
    print(n , end=", ")
