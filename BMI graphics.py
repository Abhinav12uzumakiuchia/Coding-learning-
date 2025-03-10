import turtle
your_height = turtle.numinput("height","what is your height?")
your_weight = turtle.numinput("weight","what is your weight?")
BMI = your_weight/(your_height/100)**2
print("your BMI is =",BMI)
