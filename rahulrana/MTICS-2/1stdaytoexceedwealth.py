# Compute the number of the first day when your wealth will exceed *target_amount*,
# if you start with *starting_amount* of cash and earn *earn_percent* percents every day
def DayToReachTarget(starting_amount, earn_percent, target_amount):
    day = 1
    amount = starting_amount
    day_multiplier = (1 + (earn_percent) / 100.0)
    while amount < target_amount:
        day += 1
        amount = amount * day_multiplier
    return day

def PrintFirstDay(starting_amount, earn_percent, target_amount):
    print("If you start with $%d and earn %d%% each day, you will have more than $%d on day %d for the first time!" %
          (starting_amount, earn_percent, target_amount, DayToReachTarget(starting_amount, earn_percent, target_amount)))

# Prints when you will get more than $1000000 for the first time, if you start with $1000
# and earn 2% every day.
PrintFirstDay(1000, 10, 1000000)