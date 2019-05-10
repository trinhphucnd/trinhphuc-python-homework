n = input('Enter your balance :')
m = str(n.lstrip('0'))

ko = list(m)
ko.insert(0,"$")

count = 0
stt = -4
loop = True

while loop:
    ko[stt] = ko[stt] + ","
    stt -= 3
    if stt < -len(ko) + 1:
        loop = False


for i in range (len(ko)):
    print(ko[count],end="")
    count += 1
    