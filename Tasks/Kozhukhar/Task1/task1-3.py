speed = float(input("Please enter speed in kilometers per houre: "))


def kmhoure_msec(speed):
    """Convert kilometers per hour to meters per second"""
    return speed / 3.6


print(f"{speed} km/h is {kmhoure_msec(speed):.2f} m/s")
