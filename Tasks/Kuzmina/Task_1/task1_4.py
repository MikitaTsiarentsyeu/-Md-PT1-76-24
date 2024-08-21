print ("I convert BYN to the real currency of the country, that is $.")


tem = float(input ("Enter the dollar exchange rate at the time of conversion:"))
byn = float(input ("Enter BYN to get a quote:"))
res = tem * byn


print ("At your place", byn,"rubles. You can buy BYN for your amount", res, "$")