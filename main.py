# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
bmi = int(weight)/int(height**2)
#Write your code below this line 👇
if bmi <= 18.5:
  print("you are underweight")
elif bmi < 25:
  print("normal")
elif bmi < 30:
  print("slightly overwieght")
elif bmi < 35:
  print("obese")
elif bmi > 35:
  print("clinically obese!!")



