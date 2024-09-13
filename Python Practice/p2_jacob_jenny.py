# p2_jacob_jenny.py

# a) Tuples with distinct integers a, b, c, d such that a^2 + b^2 = c^2 + d^2
result_a = [(a, b, c, d) for a in range(1, 11) for b in range(1, 11)
            for c in range(1, 11) for d in range(1, 11) if a != b != c != d and a**2 + b**2 == c**2 + d**2]

# b) Tuples with lowercase version and length of strings with length < 5
strings = ['One', 'SEVEN', 'three', 'two', 'Ten']
result_b = [(s.lower(), len(s)) for s in strings if len(s) < 5]

# c) Full names formatted as "Firstname M. Lastname"
names = ['Mila J. Austin', 'Jake M. Fey']
result_c = [f"{name.split()[0]} {name.split()[1][0]}. {name.split()[-1]}" for name in names]

# d) Anagram pairs from lst1 and lst2
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]
result_d = [(w1, w2) for w1 in lst1 for w2 in lst2 if sorted(w1.lower()) == sorted(w2.lower())]

# e) Dictionary mapping strings to their lengths
s = ['one', 'two', 'three']
result_e = {string: len(string) for string in s}

# f) Dictionary mapping index to vowel characters in a given text
text = "Hello world"
vowels = "aeiou"
result_f = {i: c for i, c in enumerate(text) if c.lower() in vowels}

# Print results
print("a) Tuples with distinct integers a, b, c, d:", result_a)
print("b) Tuples with lowercase version and length of strings with length < 5:", result_b)
print("c) Full names formatted as 'Firstname M. Lastname':", result_c)
print("d) Anagram pairs from lst1 and lst2:", result_d)
print("e) Dictionary mapping strings to their lengths:", result_e)
print("f) Dictionary mapping index to vowel characters in the given text:", result_f)
