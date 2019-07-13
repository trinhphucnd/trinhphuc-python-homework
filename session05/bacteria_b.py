count = int(input('How many B bacteria are there ? '))
minute = int(input('How much time in minute will we wait ?'))
x = minute/2
y = count * (2**x)
print("After {0} minutes , we would have {1} bacteria B ".format(minute,y))