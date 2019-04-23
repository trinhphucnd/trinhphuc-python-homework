P = 10000
n = 12
r = 0.08
t = int(input("the number of years t that the money will be compounded ?"))
A=P*((1+r/n)**(n*t))
print("The final amount after t years :", A)