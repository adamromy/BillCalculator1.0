# BillCalculator1.0

##Bill+Tip Calculator

print('Welcome to BillCalc 1.0\n\n')
num_people=0
bill=0.00
percent = 0
accepted_percent = range(10,101)

#get some input

num_people =int(input('How many people are paying?:\t'))
bill =float(input('How much is the bill?:\t$'))

#minimal error catch

while percent not in accepted_percent:
    percent=float(input('How much do you intend to tip:\t%'))
    if percent in accepted_percent:
        print('Splendid!')
    else:
        print('Whoops, are you sure thats possible?')
        

percent = percent/100
tip=bill*percent

#rounds tip to nearest hundreth for readability

tip = round(tip,2) 

total=bill+tip

#how much does each person pay?

person_pays = total / num_people
person_pays = round(person_pays,2)

print('\nThe tip: ${}\nEach person should pay: ${}'.format(tip,person_pays))







############################### Bill Calc as a function  #################################

##bill+tip calc as a func

def bill_tip_calc(num_people, bill, tip):
    
    tip = tip/100
    total_bill = bill*tip +bill
    person_pays = total_bill/num_people
    print(f'Each person should pay ${person_pays}')
    return 


