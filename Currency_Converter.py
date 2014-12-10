allowable = ["GBP", "USD", "EUR", "JPN"]
Rates = [1,3.25,1.20, 180]
Pounds = 'GBP'
Dollars = 'USD'
Yen = 'JPN'
Euro = 'EUR'
print("Welcome to the Currency converter!”)






CF = none
#
while CF not in range(len(allowable)):
    print('What currency you wish to convert from?')
    for index, currency in enumerate(allowable):
        print ('enter {0} for {1}'.format(index, currency))
    CF = input("Type the currency you wish to convert from ")
CF = int(CF)

CT = None
while CT not in range(len(allowable)):
    print('Type the currency you wish to convert to')
    for index, currency in enumerate(allowable):
        print ('enter {0} for {1}'.format(index, currency))
    CT = input("Type the currency that you wish to convert to ")
CT = int(CT)

 AM= float(input("Type the amount of currency you wish to convert "))

amount = AM/rates[var1] *rates[var2]
print(' The converted amount is {0} {1}'.format(amount,allowable[CT]))
