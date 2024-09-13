#(a)
class RndSeq:
    def __init__(self, x0, n):
        self.x0 = x0
        self.n = n
        self.count = 0
        self.m = 2**32
        self.a = 22695477
        self.c = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= 0 and self.count >= self.n:
            raise StopIteration
        else:
            self.count += 1
            self.x0 = (self.a * self.x0 + self.c) % self.m
            return self.x0

#(b)
def rnd_gen(x0, n):
    count = 0
    m = 2**32
    a = 22695477
    c = 1

    while True:
        if n >= 0 and count >= n:
            break
        else:
            count += 1
            x0 = (a * x0 + c) % m
            yield x0


def main():
    #RndSeq class
    rnd_seq = RndSeq(2, 10)
    print([i for i in rnd_seq])

    #rnd_gen generator
    print([i for i in rnd_gen(2, 10)])


if __name__ == "__main__":
    main()


