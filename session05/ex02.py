number = [1, 6 ,8 ,1 ,2 ,1 ,5 , 6]
n = int(input('Enter a number? '))
check =[]
count = 0
for i in range(len(number)): 
    if number[count] == n:
        check.append(number[count])
    count += 1
ok = len(check)
print ('{0} appears {1} times in my list '.format(n , ok))