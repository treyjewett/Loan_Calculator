import math

def cal_screen():
    print('What do you want to calculate?')
    print('''type "n" - for count of months,
type "a" - for annuity monthly payment,
type "p" - for credit principal:''')

def month_count():
    print('Enter credit principal:')
    p = float(input())
    print('Enter monthly payment:')
    mo_pay = int(input())
    print('Enter credit interest:')
    interest = float(input())
    i = interest / 1200
    n = float(math.log((mo_pay / (mo_pay - (i * p))), (1 + i)))
    years = float(n / 12)
    months = float(n % 12)
    if years < 1:
        if int(months) == 1:
            print('You need 1 month to repay this credit!')
        else:
            print('You need {} months to repay this credit!'.format(round(months)))
    elif round(years) == 1:
        print('You need 1 year to repay this credit!')
    elif round(years) > 1:
        if round(months) == 0 or round(months) == 12:
            print('You need {} years to repay this credit!'.format(round(years)))
        elif months != 0:
            print('You need {} years and {} months to repay this credit!'.format(int(years), (math.ceil(n % 12))))

def annuity_payment():
    print('Enter credit principal:')
    p = float(input())
    print('Enter count of periods:')
    n = int(input())
    print('Enter credit interest:')
    interest = float(input())
    i = interest / 1200
    a = math.ceil(p * (i * ((1 + i)**n) / ((1 + i)**n - 1)))
    print('Your annuity payment = {}!'.format(a))

def credit_principal():
    print('Enter monthly payment:')
    mp = float(input())
    print('Enter count of periods:')
    n = int(input())
    print('Enter credit interest')
    interest = float(input())
    i = interest / 1200
    p = round(mp / (((i * (1 + i)**n)) / (((1 + i)**n) - 1)))
    print('Your credit principal = {}!'.format(p))

cal_screen()
cal = input()

if cal == "n":
    month_count()

if cal == "a":
    annuity_payment()

if cal == "p":
    credit_principal()
