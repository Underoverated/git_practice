hrs = input('How many hours? ')
rte = input('At what rate? ')
hrs = float(hrs)
rte = float(rte)

if hrs >40.0:
    hrsx = hrs - 40.0
    pay = (hrs*rte) + (hrsx * (rte*0.5))
else:
    pay = rte*hrs

print(pay)
