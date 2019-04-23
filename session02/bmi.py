height =int(input("Your height (cm) :"))
weight =int(input("Your weight (Kg) :"))

bmi = (weight)/((height* height)/10000)

if bmi < 16 :
  print("Severely underweight")
elif bmi <= 18.5 :
  print("Underweight")
elif bmi <=25 :
  print("Normal ")
elif bmi <= 30 :
  print("Overweight")
else:
  print("Obese")
