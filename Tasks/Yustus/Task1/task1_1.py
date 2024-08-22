# 1.Write a program that converts Celsius to Fahrenheit, ask a user for the Celsius value.

val_celsius = (float
               (input("To convert Celsius to Fahrenheit enter yor value in Celsius : "))
               )

"""The round() function returns a floating point number that is a rounded version of the specified number,
 with the specified number of decimals."""

val_fahrenheit = round((val_celsius * 9 / 5) + 32)

print("Fahrenheit value is : ", val_fahrenheit)
