# a
for i in range(8):
    for j in range(8):
        if j>i :
            print(' ', end="")
        else :
            print('*',end ="")
    print()

print("-"*20)

# b
for i in range(8):
    for j in range(8):
        if j>=8-i :
            print(' ', end="")
        else :
            print('*',end ="")
    print()

print("-"*20)
# c
for i in range(8):
    for j in range(8):
        if j<i :
            print(' ', end="")
        else :
            print('*',end ="")
    print()

print("-"*20)

# d
for i in range(8):
    for j in range(8):
        if j<=6-i :
            print(' ', end="")
        else :
            print('*',end ="")
    print()