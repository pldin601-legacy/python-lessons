__author__ = 'roman'

money = {
    500: 100,
    200: 100,
    100: 100,
    50: 500,
    10: 500,
    5: 500
}

while True:
    print("Available banknotes: " + ", ".join(str(key) for key in money if money[key] > 0))
    num = input("How many money you want to get? ")
    print(num)
