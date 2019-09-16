
carb = 4
prot = 4
fats = 9




def calories(cal):
    print('Your calories are:', cal)

def bmrcalcmale(weight,height,age):
    bmrmale = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    return bmrmale

def bmrcalcfemale(weight,height,age):
    bmrfemale = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return bmrfemale

def activitylvl(actlvl)
    cal = bmr * actlvl
    return cal


print('Hello!')
print('Today we are going to find out how many calories you should be eating in a day')
