def hex_system(x):
    x = int(x)
    letters = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    b = ''
    while x >= 16:
        a = x % 16
        if a >= 10:
            a = letters[a]
        b = str(a) + b
        x = x // 16
    else:
        b = str(x) + b
    return b
def checking(x):
    mistake = 'Error. The number must be in the interval [0;255]'
    if x.isdigit():
        if 0 <= int(x) <= 255:
            return True
    print(mistake)
    return False
num = '#'
entering = 'Enter index of {} color which must be in the interval [0;255]'
for i in ('red', 'green', 'blue'):
    while True:
        x = input(entering.format(i))
        if checking(x):
            num += hex_system(x).zfill(2)
            break
print('Hex representation of color is: ' + num)
