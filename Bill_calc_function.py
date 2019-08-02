def bill_tip_calc(num_people, bill, tip):
    tip = tip/100
    total_bill = bill*tip +bill
    person_pays = total_bill/num_people
    print(f'Each person should pay ${person_pays}')
    return 

bill_tip_calc(5,3000.15,15)

