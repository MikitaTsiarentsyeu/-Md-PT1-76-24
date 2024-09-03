# 3.Write a program that converts kilometers per hour to meters per second, ask a user for the speed.

speed_kmh = float(
    input("Enter a speed value in km/h: ")
)
speed_ms = round(
    float(speed_kmh * 1000 / 3600), 2)
print(speed_ms, "m/s")
