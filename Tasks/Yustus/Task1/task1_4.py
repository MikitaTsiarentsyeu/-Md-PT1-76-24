# 4.Write a program that converts some amount of money from USD to BYN, ask a user for the amount, store the ratio.

ratio_byn_usd = float(3.214)
ratio_byn_eur = float(3.473)
ratio_byn_rub = float(3.635 / 100)

tipe_currency = input("What type of currencies to convert (USD,EUR,RUB) : ")

amount = float(input("Enter amount of " + tipe_currency + ":"))

if tipe_currency == "USD":
    amount_byn = float(ratio_byn_usd * amount)
    print("You have : ", amount_byn)
if tipe_currency == "EUR":
    amount_byn = float(ratio_byn_eur * amount)
    print("You have : ", amount_byn)
if tipe_currency == "RUB":
    amount_byn = float(ratio_byn_rub * amount)
    print("You have : ", amount_byn)








