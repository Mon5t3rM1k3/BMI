
#bmi calculation function

def bmi(weight,height):
    
    #conver height in meter

    height_in_meter = height * 0.3048

    bmi = weight / (height_in_meter * height_in_meter)

    if bmi < 16:
        print('Severe Thinness')
    elif  16 <= bmi < 17:
        print('Moderate Thinness')
    elif  17 <= bmi < 18.5:
        print('Mild Thinness')
    elif 18.5 <= bmi < 25:
        print('Normal')
    elif 25 <= bmi < 30:
        print('Over weight')
    elif 30 <= bmi < 35:
        print('Obese Class I')
    elif 35 <= bmi < 40:
        print('Obese Class II')
    else:
        print('Obese Class III')

    print(bmi)

bmi(
    weight = float(input("Enter your weight in KG : "))
    ,height = float(input("enter your height in ft.in : "))
    )

