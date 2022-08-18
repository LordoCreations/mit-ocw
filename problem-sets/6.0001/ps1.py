def sinput(query, type=int, edit=False):
    try:
        if edit:
            v = edit(input(query))
            if not v: raise ValueError
            else: return v
        else:
            return type(input(query))
    except KeyboardInterrupt:
        exit()
    except:
        print('Invalid Input - Try Again')
        return sinput(query, type, edit)


def percent(v):
    try:
        return int(v[:-1])/100
    except:
        return None

total_cost = sinput('What is the cost of your dream home?   ')
portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = sinput('What is your current annual salary?   ')
portion_saved = sinput('What percentage of your salary will go towards this house?   ', edit=percent)

montly_salary = annual_salary/12

months = 0
i = True
while current_savings<=total_cost:
    months += 1
    current_savings *= 1+r/12
    current_savings += montly_salary*portion_saved
    if current_savings >= total_cost*portion_down_payment and i:
        print(f'It will take {months} month(s) for you to have enough money to pay the down payment for this house.')
        i = False

print(f'It will take {months} month(s) for you to have enough money to pay for this house.')