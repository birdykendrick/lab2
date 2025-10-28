def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    #Add code here to calculate BMI
    BMI = weight / (height * height)

    print ("BMI = " + str(BMI))

    if BMI < 18.5:
        print("Under weight")
    elif BMI >= 18.5 and BMI <= 25.0:
        print("Normal weight")
    else:
        print("Overweight")
calculate_bmi(weight=60, height=1.80)