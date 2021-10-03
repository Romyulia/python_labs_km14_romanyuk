age = float(input('Enter the number of calendar years '))
if age < 0:
    print('Error. The number is negative')
elif age >= 0 and age <= 2:
    dogs_age = age*10.5
    print("The dog's age is:" + "%.2f" % dogs_age)
else:
    dogs_age = 2*10.5+4*(age-2)
    print("The dog's age is:" + "%.2f" % dogs_age)