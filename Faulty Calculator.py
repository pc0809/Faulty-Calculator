# 45 * 3 = 542      56+9=75      56/6=4

def Calc():

    x = int(input('Enter First Number:'))
    y = int(input('Enter Second Number:'))

    print('1. +\n2. -\n3. *\n4. /\n5. Modulo\n6. Square')
    z = int(input('Choose Operator:'))

    if x == 45 and y == 3 and z == 3:
        print("Your answer:",542)
    elif x == 56 and y == 9 and z == 1:
        print("Your answer:",75)
    elif x == 56 and y == 6 and z == 4:
        print("Your answer:",4)
    elif z == 1:
        print("Your answer:",x + y)
    elif z == 2:
        print("Your answer:",x - y)
    elif z == 3:
        print("Your answer:",x * y)
    elif z == 4:
        print("Your answer:",x / y)
    elif z == 5:
        print("Your answer:",x % y)
    elif z == 6:
        print("Your answer:",x ** y)
    else:
        print('Invalid Operator!')

Calc()

for i in range(50):
    a = str(input("Want to calculate again: YES=y or NO=n: "))

    if a == 'y':
        Calc()
    elif a == 'n':
        print('Thank you!')
        break
    else:
        print('Invalid Option!')