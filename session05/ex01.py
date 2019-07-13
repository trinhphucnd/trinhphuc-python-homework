backpack = ['xylophone', 'dagger', 'bedroll', 'bread loaf']
value = [500]
inventory = {
    'gold' : value,
    'pouch' :['flind' ,'twine', 'gemstone'],
    'backpack': backpack ,
}
inventory['pocket'] = ['seashell', 'stranger berry' , 'lint']
print(inventory)
backpack.remove('dagger')
value.append(50)
print(inventory)
