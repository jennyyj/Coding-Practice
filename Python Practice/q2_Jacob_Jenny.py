from itertools import islice, filterfalse
from functools import reduce

def rnd_gen(x0, n, max_value=None):
    count = 0
    m = 2**32
    a = 22695477
    c = 1

    while True:
        if max_value is not None and count >= max_value:
            break
        elif n >= 0 and count >= n:
            break
        else:
            count += 1
            x0 = (a * x0 + c) % m
            yield x0

def gen_rndtup(m):
    rnd_generator = rnd_gen(1, -1)

    while True:
        a = next(rnd_generator) % m
        b = next(rnd_generator) % m
        if a > b:
            a, b = b, a
        yield (a, b)

def main():
    #use gen_rndtup
    gen = gen_rndtup(100)
    for _ in range(5):
        print(next(gen))

    #(b)
    print("b.")
    gen = gen_rndtup(10)
    filtered_gen = filterfalse(lambda tup: sum(tup) < 6, gen)
    result = list(islice(filtered_gen, 8))
    print(result)
    
    
    #(c)
    print("c.")
    rnd_gen_a = rnd_gen(1, -1)
    rnd_gen_b = rnd_gen(2, -1)
    for _ in range(10):
       a = next(rnd_gen_a)
       b = next(rnd_gen_b)
       print("a:", a, "b:", b)
       if a <= b <= 100:
           print((a, b))
    
    #(d)
    print("d.")
    rnd_gen_13 = rnd_gen(1, -1)
    divisible_by_13 = filter(lambda x: x % 13 == 0, rnd_gen_13)
    first_10_numbers = islice(divisible_by_13, 10)
    print(list(first_10_numbers))
    
    #(e)
    print("e.")
    gen = gen_rndtup(10)
    filtered_gen = filter(lambda tup: sum(tup) >= 5, gen)
    first_10_tuples = islice(filtered_gen, 10)
    result = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), first_10_tuples)
    print(result)

if __name__ == "__main__":
    main()



