n = input("Mảng đầu vào : ")
words = n.strip().split(" ")

numbers = []

for word in words :
    numbers.append(int(word))

softed = []

for i in range (len(numbers)):
    softed.append(max(numbers))
    numbers.remove(max(numbers))

print(softed)