n = int(input("Enter a number :"))

for i in range(0,n):
  for j in range(0,n):
    m=i+j
  

    if m%2 == 0:
      print("1", end=" ")
    else :
      print("0", end=" ") 
    
   
  print()