a=float(input("Enter your weight(in Kg):"))
b=float(input("Enter your height(in meters):"))
d=a/(b*b)
c=round(d)
if(c<18.5):
    print(f"Your BMI is {c} and you are underweight")
elif(c<25):
    print(f"Your BMI is {c} and you have a normal weight")
elif(c<30):
    print(f"Your BMI is {c} and you are slightly overweight")
elif(c<35):
    print(f"Your BMI is {c} and you are obese")
else:
    print(f"Your BMI is {c} and you are clinically obese")