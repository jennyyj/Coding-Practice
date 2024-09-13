import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
    xmin, xmax = domain
    xs = [xmin + (xmax - xmin) * i / (ns - 1) for i in range(ns)]
    ys = []

    print(f"{'x':<10}{'y':<10}")
    print("-" * 20)

    for x in xs:
        y = eval(fun_str)
        ys.append(y)
        print(f"{x:<10.4f}{y:<10.4f}")

    plt.plot(xs, ys, label=f"{fun_str}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function Plot')
    plt.legend()
    plt.show()

fun_str = input("Enter function with variable x: ")
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
ns = int(input("Enter the number of samples: "))

plot_function(fun_str, (xmin, xmax), ns)
