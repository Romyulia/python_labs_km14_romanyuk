from exp_root.exponentation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, ln, lg


def check(x):
    while True:
        if type(x) != int:
            try:
                x = int(x)
                break
            except ValueError:
                x = input('Input is invalid. Enter the correct number: ')
    return x


def positive(a):
    a = check(a)
    while True:
        if a <= 0:
            a = check(input('Input is invalid. Enter the correct number: '))
        else:
            break
    return a


def main():
    print("Hello user! \nTo select the desired function read the menu below:\n"
          "To calculate the factorial enter 1 \nTo calculate the square of the number enter 2\n"
          "To calculate the cube of number enter 3 \nTo calculate the square root of the number enter 4\n"
          "To calculate the cubic root of the number enter 5 \nTo calculate the logarithm enter 6\n"
          "To calculate the natural logarithm enter 7 \nTo calculate the decimal logarithm enter 8")
    choose = check(input('Enter the function number: '))
    if choose == 1:
        f = positive(input('Enter a positive number : '))
        print('The factorial of {} is {}.'.format(f, fact(f)))
    elif choose == 2:
        s = check(input('Enter a number : '))
        print('The square of {} is {}.'.format(s, exp2(s)))
    elif choose == 3:
        c = check(input('Enter a number : '))
        print('The cube of {} is {}.'.format(c, exp3(c)))
    elif choose == 4:
        r2 = positive(input('Enter a positive number : '))
        print('The square root of {} is {}.'.format(r2, root2(r2)))
    elif choose == 5:
        r3 = check(input('Enter a number : '))
        print('The cubic root of {} is {}'.format(r3, root3(r3)))
    elif choose == 6:
        a = positive(input('Enter the base of logarithm : '))
        while True:
            if a == 1 or a == 0:
                a = positive(input('Input is invalid. Enter the base of logarithm : '))
            else:
                b1 = positive(input('Enter a positive number : '))
                while True:
                    if b1 == 0:
                        b1 = positive(input('Enter a positive number : '))
                    else:
                    print('The logarithm is {}'.format(log(a, b1)))
                    break
                break
    elif choose == 7:
        b2 = positive(input('Enter a positive number : '))
                while True:
                    if b2 == 0:
                        b2 = positive(input('Enter a positive number : '))
                    else:
                        print('The natural logarithm is {}.'.format(ln(b2)))
                        break
    elif choose == 8:
        b3 = positive(input('Enter a positive number : '))
            while True:
                if b3 == 0:
                    b3 = positive(input('Enter a positive number : '))
                else:
                    print('The decimal logarithm is {}.'.format(lg(b3)))
                    break
    else:
        print('You enter a wrong number.')


if __name__ == '__main__':
    main()

