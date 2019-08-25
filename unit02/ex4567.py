n = int(input('Enter a Number : '))
# count = 1
# for i in range(1,n+1):
#     count*=i
# print(count)

# total = 0
# for i in range(1,n+1):
#     total += (1/i)
# print(total)

numerator = 0
denominator = 1
total = 0
for i in range(1,n+1):
  
    numerator = i
    denominator *= i
  
    total += (numerator/denominator)

print(total)