speed = int(input('Enter the wind speed '))
if speed < 0:
    print('Error. The number is negative.')
elif speed >= 0 and speed < 137:
    print('Potential damage is minor.')
elif speed >= 137 and speed < 177:
    print('Potential damage is moderate.')
elif speed >= 177 and speed < 217:
    print('Potential damage is considerable.')
elif speed >= 217 and speed < 266:
    print('Potential damage is severe.')
elif speed >= 266 and speed < 322:
    print('Potential damage is devastating.')
else:
    print('Potential damage is incredible.')