#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COP4045 Python Programming
Additional examples from the Ch.16 material and elements of 
functional programming in Python:
    Generator expressions, generators, composing geerators, 
    lambda expressions, higher order functions, etc.
"""


"""
Try solving the problems without peeking at the solutions.


1. Write a generator expression ge1 for a sequence of tuples (i, i**2)
with i from 1 to 100 if i is divisible to integer variables n 
(initialized earlier to 6) and m (m==7).
Print the numbers from ge1 as a list.


2. Assume names is a sequence of strings. Write a generator expression ge2
for the sequence of strings in names converted to lowercase that have length
less then 5 characters and that end with a vowel.
Print the strings from ge2 as a list.

3. Suppose we have a variable with foods and their scores given by a 
food critic, and another one for colors:
    
foods = {"pizza": 7, "ham": 8, "apple pie": 8, "lasagna": 5, "rolls": 6}
colors = ["red", "green"]
 
Write a generator expression ge3 that produces all combinations of 
"color food name" strings for foods with scores above 7.
Print the tuples from ge2 as a l

------------------------------------------------------------------------

4. Write a generator called take_while(seq, p) that yields objects x from 
iterable seq for as long as predicate p is True, i.e. while p(x) is True.

Write an expression that uses take_while to print all Fibonacci numbers less 
that n=1000. To check if a number is less than n, first use a function
and then rewrite the expression using a lambda expression.


5. Write a generator called collatz_numbers(n0) that generates a Collatz 
series.  n0 is the first term.
From https://en.wikipedia.org/wiki/Collatz_conjecture  :
"each term is obtained from the previous term as follows: if the 
previous term is even, the next term is one half of the previous term. 
If the previous term is odd, the next term is 3 times the previous term plus 1.
The Collatz conjecture is that these sequences always reach 1, no matter 
which positive integer is chosen to start the sequence."

Use the take_n generator to print the first 50 numbers from the Collatz sequence
that starts with 123. Do you notice something special?

Use the take_while generator to print the Collatz sequence that starts with 123.


6. Write a function length(seq) that returns the length of the sequence seq.

Write an expression with length() that prints how many Fibonacci numbers 
are less than a 1,000,000. Use a lambda expression.


7. Write an expression that uses a sequence of strings called names and that 
generates the original strings if they start with a vowel or changes them to 
an uppercase version if they don't start with a vowel. 
Your expression must use map() and a lambda expression. 

E.g. for names = ["Alice", "Bob", "Charlie", "Dan", "Eve"]
it generates sequence 'Alice', 'BOB', 'CHARLIE', 'DAN', 'Eve'


8. Consider a list of (student_name, gpa) tuple sequence called records.
Write code (can be more than one expression) 
that generates the sequence of student names (in variable sorted_students )
that begin with a letter in the A ... M interval in ascending order of their grade.
It must use map() and filter().


# ---------------------------------------------------------------

9. Use the functools.reduce function to compute the maximum of a 
sequence of numbers. Use a lambda expression.


10. Use the functools.reduce function to compute the average of a 
sequence of numbers without converting it to a list.
Hint: use a tuple to represent (partial_sum, partial_count) and an update 
function that computes the next tuple that is passed forward towards the
end of the sequence. 


11. Consider a variable called lst_text with a list of sentences:
    
lst_text = ["Four score and seven years ago our fathers brought forth",
        "on this continent a new nation, conceived in liberty,",
        "and dedicated to the proposition that all men are created equal."]

Write an expression using map and reduce to compute the total number of words 
included in that list.

"""    


# 1.
n = 6
m = 7
ge1 = ((i, i**2) for i in range(1, 101) if i % m == 0 and i % n == 0)
print("\n1. ", list(ge1))


# 2.
names = ["Ana", "Tayler", "Bert", "Zack", "Jose", "Dan", "Mike"]

ge2 = ( s.lower() for s in names if len(s) < 5 and s[-1] in "aeiou")
print("\n2. ", list(ge2))


# 3.
foods = {"pizza": 7, "ham": 8, "apple pie": 8, "lasagna": 5, "rolls": 6}
colors = ["red", "green"]

ge3 = ( f"{color}:{food}" for (food, score) in foods.items() if score > 7
       for color in colors )
print("\n3. ", list(ge3))



# ---------------------------------

import itertools as itt
import functools

# ==============================================================
def take_n(n, seq):
    i = 0
    for x in seq:    # access the sequence with "for"
        if i < n:    # more
            yield x
            i += 1   
        else:
            break    # reached n. "return" will stop the iteration in caller.

def gen_filter(predicate, iterable):
    for x in iterable:
        if predicate(x):
            yield x

# the general pattern for a combining generators/sequences:
def gen_transformer(fun, iterable):
    for x in iterable:
        # do something with x:
        yield fun(x)

def myrange(start, stop, step=1):
    """Requires step >= 0"""
    i = start
    while i < stop:
        yield i
        i += step


# a generator that outputs 0,1,2,.... forever
def gen_naturals():
    i = 0
    while True:
        yield i
        i += 1

def gen_infinite_fibonacci(f0=0, f1=1):
    while True:
        yield f0
        f0, f1 = f1, f0+f1

# ==============================================================


# 4.
def take_while(seq, p):
    for x in seq:
        if not p(x):
            break
        yield x

n = 1000

def less_then_n(x):
    return x < n

print("\n4. Fibonacci numbers < {n} with function:")
for f in take_while(gen_infinite_fibonacci(), less_then_n):
    print(f, end=", ")
    
print("\n\n4. Fibonacci numbers < {n} with lambda expression:")
for f in take_while(gen_infinite_fibonacci(), lambda x: x < n):
    print(f, end=", ")


# 5.
def collatz_numbers(n0:int):
    m = n0
    while True:
        yield m
        if m % 2 == 0:
            m = m // 2 
        else:
            m = 3 * m + 1

n0 = 123
count = 50
lst = list(take_n(count, collatz_numbers(n0)))
print(f"\n\n5. Collatz numbers with take_n({count},...), n0={n0}, {lst}\n") 

lst = list(take_while(collatz_numbers(n0), lambda x: x != 1))
print(f"\n\n5. Collatz numbers != 1, n0={n0}, {lst}\n") 


# 6.
def length(seq):
    i = 0
    for x in seq:
        i += 1
    return i


n = 1000000    
count_less_n = length(take_while(gen_infinite_fibonacci(), lambda x: x < n))

print(f"\n\n6. Fibonacci numbers < {n}: {count_less_n}\n") 


# 7.
names = ["Alice", "Bob", "Charlie", "Dan", "Eve"]
names2 = map(lambda s: s if s[0].lower() in "aeiou" else s.upper(), names)

print(f"\n\n7. {list(names2)}")


# 8.
records = [("Sue", 80), ("Jose", 85), ("Spencer", 84), 
           ("Alice", 90), ("Jenny", 95), ("Bob", 75)]

filtered_records = filter(lambda tup: 'a' <= tup[0][0].lower() <= 'm', records)
sorted_records = sorted(list(filtered_records), key=lambda tup: tup[1])
sorted_students = map(lambda tup: tup[0], sorted_records)

print(f"\n\n8. {list(sorted_students)}")


# 9.
import functools

numbers = [90, 80, 100, 40]

# could write max(maxn, current) instead of the if expression
max_number = functools.reduce(lambda maxn, current: current if current > maxn else maxn, numbers)

print(f"\n\n9. max number is {max_number}. max() returns {max(numbers)}") 


# 10. 
numbers = [90, 80, 100]

# the tuple argument tup represents (partial_sum, partial_count)
# the anonymous function "updates" the tuple that is passed forward based 
#    on x, the current element of the sequence.
(summ, n) = functools.reduce(lambda tup, x: (x + tup[0], 1 + tup[1]), numbers, (0.0, 0))

avg = summ / n if n > 0 else None     # can't divide by 0
print(f"\n\n10. reduce result is {(summ, n)}, avg={avg}")


# 11.
lst_text = ["Four score and seven years ago our fathers brought forth",
        "on this continent a new nation, conceived in liberty,",
        "and dedicated to the proposition that all men are created equal."]

cnt_words = functools.reduce(lambda summ, x: summ + x,       # simple addition (x is the current seq. element)
    map(lambda sentence: len(sentence.split()), lst_text))   # sequence of word counts

print(f"\n\n11. map reduce word count {cnt_words}")
