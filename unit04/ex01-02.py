n = input("Enter a sequence of number, separated by space : ")

words = n.strip().split(" ")

numbers = []

for word in words :
    numbers.append(int(word))

print(numbers)
print("Trung binh cong : " , sum(numbers)/len(numbers))
print("Max of senquence: " , max(numbers)) 
