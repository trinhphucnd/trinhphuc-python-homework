n = input("Your full name ? ")
m = n.replace("  "," ").strip(' ').lower().split()
name =[]
count = 0

while True :
    
    name.append(m[count].capitalize())
    count += 1

    if count == len(m):

        break
        print(name[count-1])


if len(m) == 3:
    print(name[0],name[1],name[2])
elif len(m) == 2:
    print(name[0],name[1])
elif len(m) == 4:
    print(name[0],name[1],name[2],name[3])



