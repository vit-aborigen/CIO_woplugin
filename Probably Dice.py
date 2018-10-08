from math import factorial

def binom_coef(n, k):
    return factorial(n) // factorial(k) // factorial(n-k)

def probability(dice_number, sides, target):
    # https://www.lucamoroni.it/wp-content/ql-cache/quicklatex.com-e808aa7d3a5e459c20c0297d894cdbab_l3.svg formula was used
    if target > sides * dice_number: return 0

    solutions_amount = 0
    Kmax = (target - dice_number) // sides

    for step in range(Kmax + 1):
        solutions_amount += (-1)**step * binom_coef(dice_number, step) *\
                            binom_coef(target - sides*step - 1, target - sides * step - dice_number)

    return round(solutions_amount / sides**dice_number, 4)

print(probability(1, 2, 999))