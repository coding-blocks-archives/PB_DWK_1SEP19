


import math
pi = math.pi

def square(a):
    return a**2

def rectangle(a,b):
    return a*b

def circle(r):
    return pi*r*2

if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]
    shape = arguments[0]
    if shape == 'circle':
        print(circle(int(arguments[1])))
    elif shape == 'rectangle':
        a = int(arguments[1])
        b = int(arguments[2])
        print('Area of rectangle:{}'.format(rectangle(a,b)))
    elif shape == 'square':
        print(square(int(srguments[1])))
    else:
        print('this option is not available.')
