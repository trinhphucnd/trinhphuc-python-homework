# Giải phương trình bậc 1

# a = int(input('Nhập a , pt có dạng ax+b = 0  : '))
# b = int(input('Nhập b , pt có dạng ax+b = 0  : '))


# if a == 0 and b == 0 :
#     print('Phương trình vô số nghiệm')
# elif a == 0 and b!= 0:
#     print('Phương trình vô nghiệm')
# elif a != 0 and b != 0 :
#     print('Phương trình có nghiệm là: ', -b/a ) 


###################################################################
# Giải Phương trình bậc 2

a = int(input('Nhập a (a#0) , pt có dạng ax^2 + bx + c = 0  : '))
b = int(input('Nhập b , pt có dạng ax^2 + bx + c = 0  : '))
c = int(input('Nhập c , pt có dạng ax^2 + bx + c = 0  : '))

denta  = b**2 - 4*a*c
if denta == 0 :
    print("Phương trình có nghiệm kép : ", -b/(2*a*c))
if denta != 0 :
    print("Phương trình có 2 nghiệm phân biệt : ",)
    print('X1 : ' , (-b+denta) / (2*a*c) )
    print('X2 : ' , (-b-denta) / (2*a*c) )
