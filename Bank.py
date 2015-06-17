import math

money = {
    500: 1,
    200: 1,
    100: 1,
    50: 5,
    10: 5,
    5: 5,
    2: 10,
    1: 10
}

while True:
    print("")
    print("")
    print("Available banknotes: " +
          ", ".join(str(key) + "(" + str(money[key]) + ")" for key in money if money[key] > 0))
    print("")

    try:
        num = int(input("How much money you want to get? "))
    except ValueError:
        print("Invalid value!")
        continue

    if num <= 0:
        print("You trying to deposit? Enter positive number!")
        continue

    if num % min(money.keys()) != 0:
        print("Value must be multiple of " + str(min(money.keys())))
        continue

    package = {}
    for key in sorted(money.keys(), reverse=True):
        if money[key] > 0 and num > 0:
            cnt = min(money[key], math.floor(num / key))
            num = num - key * cnt
            if 0 < cnt <= money[key]:
                package[key] = cnt

    if num == 0:
        for key in sorted(package, reverse=True):
            money[key] -= package[key]
            print("You got " + str(package[key]) + " banknote(s) of " + str(key) + " UAH")
    else:
        print("Sorry! Terminal has no enough money to satisfy you :(")