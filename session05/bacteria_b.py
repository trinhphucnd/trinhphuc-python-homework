count = int(input('How many B bacteria are there ? '))
minute = int(input('How much time in minute will we wait ?'))
if minute % 2 == 1:
    minreal = (minute/2) + 0.5
    x = minreal/2
    y = count * (2**x)
elif minute % 2 == 0 :
    minreal = minute
    x = minreal/2
    y = count * (2**x)

print("After {0} minutes , we would have {1} bacteria B ".format(minute,y))