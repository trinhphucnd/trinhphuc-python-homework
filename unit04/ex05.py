n = input("Mảng đầu vào : ")
k = int(input("Với k = "))
words = n.strip().split(" ")

numbers = []

for word in words :
    numbers.append(int(word))
numbers.remove(numbers[k])
print("mảng đầu ra :", numbers)
