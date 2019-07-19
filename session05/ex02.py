numbers = [1, 6 ,8 ,1 ,2 ,1 ,5 , 6]
n = int(input('Enter a number? '))
check = []

for numb in numbers:
    if numb == n:
        check.append(numb)
    
y = len(check)

print ('{0} appears {1} times in my list '.format(n , y))

# # use count()
# print(numbers.count(n))