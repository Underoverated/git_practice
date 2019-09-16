
total = 0

while num != 'done'
    num = input('Enter a number')
    try:
        num = float(num)
    except:
        print('bad data')
        continue

#not complete
