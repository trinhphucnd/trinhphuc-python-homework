n = int(input("Enter the number :"))

for i in range(1,n+1,1):
  for j in range(1,n+1,1):
    m=i*j
    if m<10:
      print(m,end="  ")
    else:
      print(m,end=" ")
 
   
  print()