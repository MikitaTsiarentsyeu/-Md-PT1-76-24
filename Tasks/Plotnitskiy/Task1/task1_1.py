celsius = float(
    input("Please enter the temperature in Celsius: ")
)  # используем float для получения десятичных чисел с дробной частью, запрашиваем у пользователя температуру в градусах Цельсия
fahrenheit = (celsius * 9 / 5) + 32  # переводим температуру в градусы Фаренгейта
print("The temperature in Fahrenheit is: ", fahrenheit)  # выводим результат
