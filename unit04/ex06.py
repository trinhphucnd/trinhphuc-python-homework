n = input("Mảng đầu vào : ")
words = n.strip().split(" ")

numbers = []

for word in words :
    numbers.append(int(word))
odd_numbers = []
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else :
        odd_numbers.append(number)    
print("Danh sách các số lẻ : ", odd_numbers)
print("Danh sách các số chẵn :", even_numbers)

