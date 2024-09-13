def find_Pythagorean(n):
    pythagorean_triples = []
    for a in range(1, n+1):
        for b in range(1, n+1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= n:
                pythagorean_triples.append((a, b, int(c)))
    return pythagorean_triples

def main():
    try:
        n = int(input("Enter a positive number n: "))
        if n <= 0:
            print("Please enter a positive number.")
            return

        triples = find_Pythagorean(n)

        if not triples:
            print("No Pythagorean triples found.")
        else:
            print("Pythagorean triples:")
            for triple in triples:
                print(triple)

    except ValueError:
        print("INot a positive number. Please enter a positive number.")

if __name__ == "__main__":
    main()
