n = input("Mảng đầu vào : ")
m = int(input("Nhập vào số cần kiểm tra : "))
words = n.strip().split(" ")

numbers = []

for word in words :
    numbers.append(int(word))

