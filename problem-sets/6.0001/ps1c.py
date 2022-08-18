def sinput(query, type=int, edit=False):
    try:
        if edit:
            v = edit(input(query))
            if not v:
                raise ValueError
            else:
                return v
        else:
            return type(input(query))
    except KeyboardInterrupt:
        exit()
    except:
        print('Invalid Input - Try Again')
        return sinput(query, type, edit)


def percent(v):
    try:
        return int(v.replace(" ", "")[:-1])/100
    except:
        return None

total_cost = sinput('What is the cost of your dream home?   ')
portion_down_payment = 0.25
r = 0.04
annual_salary = sinput('What is your current annual salary?   ')
#semi_annual_raise = sinput( 'What percentage will your salary raise every 6 months?   ', edit=percent)

montly_salary = annual_salary/12


def search(t, b, goal):

    mid = (t+b)/2
    months = 0
    savings = 0
    # while savings <= total_cost*portion_down_payment:
    for i in range(goal):
        months += 1
        savings *= 1+r/12
        savings += montly_salary*(mid/100)
    #print(mid, months)
    if t-b<0.001:
        return (mid, months, savings)
    if savings > total_cost:
        res = search(mid, b, goal)
        if res[0] > mid:
            return (mid, months, savings)
        else: return res

    else:
        res = search(t, mid, goal)
        if res[0] > mid:
            return (mid, months, savings)
        else: return res
res = search(100, 0, 36)
print(f"If you save {round(res[0], 3)}% of your salary, you will be able to pay the down payment of your house in {res[1]} months with {round(res[2], 2)}$")