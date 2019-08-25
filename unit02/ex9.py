k = int(input("Nhập K : "))
n = int(input('Nhập N : '))
m = int(input('Nhập M (M >= N) : '))

total = 0
for i in range (n,m):
    if i % k == 0 :
        total += i
print(total)