import matplotlib.pyplot as plt
import numpy as np
import math
import sys

def discriminant(a, b, c):
    return b**2 - 4*a*c

def calculate_solution(a, b, c):
    d = discriminant(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f'two solutions: x1={x1} x2={x2}')
        return x1, x2
    elif d == 0:
        x = -b / (2*a)
        print(f'one solution: x={x}')
        return x, x
    else:
        print('no real solutions')
        return None, None

def plot_quadratic(a, b, c, roots):
    x_opt = -b / (2*a)
    
    if roots is not None:
        x_range = np.linspace(min(roots) - 2, max(roots) + 2, 150)
    else:
        x_range = np.linspace(x_opt - 2, x_opt + 2, 150)

    y = a*x_range**2 + b*x_range + c

    plt.plot(x_range, y, label=f"{a}x^2 + {b}x + {c}")
    
    if roots is not None:
        plt.scatter(roots, [0]*len(roots), color='red', marker='o', label='Roots')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(x_opt, color='green', linestyle='--', label='Optimal x')
    
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Function Visualization')
    plt.show()

print('Enter a, b, and c for the quadratic equation ax^2 + bx + c = 0:')

while True:
    try:
        a = float(input('Enter a: '))
        b = float(input('Enter b: '))
        c = float(input('Enter c: '))

        x1, x2 = calculate_solution(a, b, c)
        plot_quadratic(a, b, c, [x1, x2] if x1 is not None else None)

        # Simulate user typing CTRL-Z on Windows to finish the program
        if a == 1 and b == -1 and c == -6:
            sys.exit()

    except ValueError:
        print('Please enter a valid number.')
