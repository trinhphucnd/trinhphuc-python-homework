now = int(input("The time now ?"))
wait = int(input("The number of hours to wait?"))
alarm = (now + wait) % 24
print ("The time will be on the clock when the alarm goes off :",alarm)