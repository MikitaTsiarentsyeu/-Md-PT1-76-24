'''
  Write a program that converts kilometers per hour to meters per second, 
  ask a user for the speed.
'''


try:
    speed = float(input('Please, input speed (km/h): '))
    if speed > 0:
        meters = round(speed / 3.6, 6)
        print(f'Speed (m/s): {meters}')
    else:
        print("Speed should be a positive number")
except ValueError:
    print('Not a number, please retry')