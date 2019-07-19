print("Month {0} : {1} pair(s) of rabbit".format(0,1))

print("Month {0} : {1} pair(s) of rabbit".format(1,2))

Fibonacci = [1,2]

count = 2

for i in range (3):
    
    Fn = Fibonacci[count-1] + Fibonacci[count-2]
    
    Fibonacci.append(Fn)
    
    count += 1
    
    print("Month {0} : {1} pair(s) of rabbit".format(count-1,Fn))


