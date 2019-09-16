def computepay(hours,rate):
    if hours >40.0:
        hrsx = hours - 40.0
        pay = (hours*rate) + (hrsx * (rate*0.5))
        return pay
    else:
        pay = rate*hours
        return pay

hours = input('Enter hours: ')
rate = input('Enter rate: ')
hours = float(hours)
rate = float(rate)

print('Pay:', computepay(hours,rate))
