height = float(input("Please enter your height in meters: "))
weight = int(input("Please enter your weight in kilograms: "))
bmi=weight/(height*height)
formatted_bmi = "{:.2f}".format(bmi)

if bmi < 18.5:
    print("Your BMI is {}, you are underweight.".format(formatted_bmi))
elif bmi < 25:
    print("Your BMI is {}, you have a normal weight.".format(formatted_bmi))
elif bmi < 30:
    print("Your BMI is {}, you are slightly overweight.".format(formatted_bmi))
elif bmi < 35:
    print("Your BMI is {}, you are obese.".format(formatted_bmi))
else:
    print("Your BMI is {}, you are clinically obese.".format(formatted_bmi))