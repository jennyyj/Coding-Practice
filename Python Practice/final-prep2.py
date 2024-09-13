#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COP 4045
Final Exam Preparation
Problems with Recursion, Iterators, Generators, Generator Expressions, 
Elements of Functional Programming, Decorators, numpy.

Created on Tue Apr 16 08:44:23 2024

@author: icardei
"""


"""

RECURSION

1.1 
Write a recursive function deep_find(lst:list, x) that returns True if object 
x is in list lst. lst may have nested lists.

Examples:
    deep_find([1,2,3], 3) returns True
    
    deep_find([1, 2, [[3, 4], 5], 6], 4) returns True

    deep_find([1, 2, [[3, 4], 5], 6], 0) returns False

1.2
Write a recursive function filter_rec(seq, p) that returns a list with
all objects x from iterable seq for which p(x) is True.

Bonus points if the function is tail-recursive.

Demonstrate the function using anonymous functions.



1.3
Write a recursive function flatten(lst:list) where the lst argument may include
as elements other lists. The function returns all elements from lst 
in a flattened list.

Example:
    flatten([1,2,[3, 4], 5, [6, [[7]]], 8]) returns [1,2,3,4,5,6,7,8].

    flatten([[[], []], []]) returns []


1.4 
One can represent a tree node in Python as a tuple with format (data, list_of_children).
For example, the root directory on a file system can be written as:

files = 
    ("/", [
        ("home", [
            ("ana", [
                ("work", [("reportA.pdf", [])]),
                ("photos", [
                    ("pic1.jpg", []), 
                    ("pic2.png", [])
                    ])])
            ("bob", [
                ("work", [("reportB.pdf", [])]),
                ("photos", [
                    ("pic1.jpg", []), 
                    ("pic2B.png", [])                
                ])]),
            ])
        ])

a) write a recursive function that returns the depth of the tree.
    
b) write a recursive function find_node(tree:tuple, p) that returns true if
    there is an object in the tree for which p(x) is True. It returns otherwise.

    Write code with lambda expressions that looks for a directory named "bob"
    and for a file named "pic1.jpg".


c) write a recursive function filter_tree(tree, p) -> list that returns a list with
    the node tuples (x, lst) for which p(x) is True.

    Write code with lambda expressions that finds all file names
    ending with extension ".png".
    
d) [HARD]
    Assume that the tree object stores directories and files like a traditional
    file system tree.
    Write a recursive function find_node_path(tree_node:tuple, path:list) that
    returns the tuple node object on the path given by the strings in the 
    path list argument.
    If the path is wrong the function returns None.
    
    Examples: 
        
    node1 = find_node_path(files, ["/", "home", "bob", "photos", "pic1.jpg"])
    node 1 is ('pic1.jpg', [])
    
    node2 = find_node_path(files, ["/", "home", "bob", "photos", "nosuchfile.jpg"])
    node2 is None
    
    node3 = find_node_path(files, ["/", "home", "ana", "photos"])
    node 3 is ('photos', [('pic1.jpg', []), ('pic2.png', [])])
    
    node4 = find_node_path(files, ["/", "home", "santa", "gifts"])
    node4 is None

--------------------------------------------------------------------------

MEMOIZATION

1.5 
Write a memoized version for the recursive function that produces 
a famous number series starting with 
0, 1, and then numbers s(n), with s(n) = 2 * s(n - 1) - s(n - 2).
What do you notice?


================================================================================


ITERABLES

2.1
Create an iterable class called Parselines that takes as constructor argument 
a string with any number of newline ('\n') characters. This class is also an
iterator that separates the text lines (by '\n') and returns them one by one.
(The "\n" characted is not included in the lines returned.)

Write some code that demonstrates how to use this class to get and print text lines.


2.2 
Create an iterable class called Parselines2 that takes as constructor argument 
a string (called text) with any number of newline ('\n') characters. 
This class returns an new iterator object from a class called LineIterator
that returns lext lines (separated by '\n') one by one, from the Parselines2
object's text property.
(The "\n" characted is not included in the lines returned.)

Write some code that demonstrates how to use this class to get and print text lines.


================================================================================

GENERATORS

3.1
Write a generator concat(it1, it2) that generates the sequence of objects from
iterable it1 followed by the sequence of objects from iterable it2.

Write some code that demonstrates how to use concat.


3.2 
Write a gen_enumerate(seq) that generates the sequence of tuples 
(0, x0), (1, x1), (2, x2), .... where the x values are from iterable seq.

Write some code that demonstrates how to use gen_enumerate.


3.3
Use generators gen_enumerate (from problem 3.2), gen_filter, take_n, and 
gen_infinite_fibonacci to print the tuple (i, f) where i is the index of the 
first Fibonacci number that exceeds a variable n = 1000000. 
Use a lambda expression.


3.4
Write a generator concat2(s1, s2, .....) that takes as argument 1 or more 
iterables and that generates all elements from s1, followed by all elements from
s2, followed by all elements from s3, etc.

Hint: review functions with variable number of parameters.


3.5
Write a generator file_words(filename:str) that opens a text file with the 
given name and generates the words in that file. Use the 'with' statement. 

================================================================================

GENERATOR EXPRESSIONS

4.1
Consider a variable lst of int numbers:
    lst = [10, 5, 11, 4, 4, 7]
Write a generator expression that greates a sequence of strings 
"select n" for all n numbers from lst >= 9.

In this case, the sequence will be "select 10","select 11".


4.2
Consider two lists like these:
    lst1 = [4, 3, 5, 1, 6]
    lst2 = [6, 2, 3]
Write a generator expression that generates all tuples (i, j), with i from lst1
and j from lst2, with i < j.

===============================================================================

FILTER, MAP and REDUCE

5.1
Suppose variable car_ads stores information about car ads in tuples
(model:str, make:str, price:int). It can be a list or some other iterable.
For example:
    car_ads = [("Civic EX", "Honda", 12000), ("Cherokee", "Jeep", "9000"),
               ("Prelude", "Honda", 10000), ("Patriot", "Jeep")].
    
Use filter, map, and functools.reduce to write code (1 or more expressions)
that computes the average price for "Honda" ads.
Use lambda expressions.


===============================================================================

DECORATORS

6.1 
Write a decorator trace_fun(f) for a function f of one argument that 
prints f's arguments before the call to f(.) and then prints the 
result after f(.) returns.

Write code that applies the decorator to a function of one argument
and then calls it.

===============================================================================

NUMPY
7.1 
a) Write an statement that creates a two-dimensional matrix A that looks like:
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
without function np.array() and without explicitly initializing each
array element.

b) Write one statement with a slice that sets all elements in A on rows 1 and 2, 
and on columns 2 and 3 to 0:
array([[0, 1, 2, 3],
       [4, 5, 0, 0],
       [8, 9, 0, 0]])
        
c) Set all 0 elements in A to -1 in one statement:
array([[-1,  1,  2,  3],
       [ 4,  5, -1, -1],
       [ 8,  9, -1, -1]])


7.2
Write code with numpy and matplotlib that displays a heat map chart with the values for
function x**2 + y**2, with both x and y in interval [-3, 3] using n = 50 steps.

Use function np.fromfunction and a lambda expression for its argument.
imshow
"""
import functools
import numpy as np
import matplotlib.pyplot as plt


# 1.1
def deep_find(lst:list, x) -> bool:
    if len(lst) == 0:
        return False
    
    found = False
    if type(lst[0]) == list:
        found = deep_find(lst[0], x)
    else:
        found = (lst[0] == x)
    return found or deep_find(lst[1:], x)


print("1.1 \n", deep_find([1,2,3], 3))

print(deep_find([1, 2, [[3, 4], 5], 6], 4))

print(deep_find([1, 2, [[3, 4], 5], 6], 0))



# 1.2.
def filter_rec(seq, p) -> list:
    magic = object()   # empty object we use as marker for end of sequence
    it = iter(seq)
    
    def helper(acc):
        x = next(it, magic)
        if x is magic:    # end of sequence??
            return acc
        
        if p(x):
            return helper(acc + [x])
        else:
            return helper(acc)
        
    return helper([])


print('\n\n1.2 ')
# print even numbers from a list
print(filter_rec([4,1,6,4,0,5,3], lambda i: i % 2 == 0))        


# 1.3
def flatten(lst:list) -> list:
    if len(lst) == 0:
        return []
    
    # recurse if the first element is another list:
    if type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    
    # first element is not a list: include it as is.
    return [lst[0]] + flatten(lst[1:])

print("\n1.3\n")
print(flatten([1,2,[3, 4], 5, [6, [[7]]], 8])) # should be [1,2,3,4,5,6,7,8].
print(flatten(flatten([[[], [[[]]]], []]))) # should be [1,2,3,4,5,6,7,8].


# 1.4 a)
# a tree leaf node is a tuple (data, [child1, child2,...])
# There is no "empty tree" concept. A node with no children looks like (x, []).
# The root node is at depth 1.

def depth(tree_node:tuple) -> int:
    (_, children) = tree_node
    if len(children) == 0:
        return 1 
    return 1 + max(depth(child_node) for child_node in children)


files = ("/", [
            ("home", [
                ("ana", [
                    ("work", [("reportA.pdf", [])]),
                    ("photos", [
                        ("pic1.jpg", []), 
                        ("pic2.png", [])
                        ])]),
                ("bob", [
                    ("work", [("reportB.pdf", [])]),
                    ("photos", [
                        ("pic1.jpg", []), 
                        ("pic2B.png", [])                
                    ])]),
                ])
            ])

print("\n\n1.4.a")
print(files)
print("file tree depth is ", depth(files))


# 1.4.b
# a verbose version
def find_node_verbose(tree_node:tuple, p) -> bool:
    if p(tree_node[0]):
        return True
    for node in tree_node[1]:
        if find_node_verbose(node, p):
            return True
    return False

print("\n\n1.4.b with verbose version\n", find_node_verbose(files, lambda filename: filename == "bob"))
print(find_node_verbose(files, lambda filename: filename == "charlie"))
print(find_node_verbose(files, lambda filename: filename == "pic1.jpg"))
    
# a short version doing the same thing:
def find_node(tree_node:tuple, p) -> bool:
    return p(tree_node[0]) or any(find_node(node, p) for node in tree_node[1])

print("\n\n1.4.b with short version\n", find_node(files, lambda filename: filename == "bob"))
print(find_node(files, lambda filename: filename == "charlie"))
print(find_node(files, lambda filename: filename == "pic1.jpg"))
    
# 1.4.c
def filter_tree(tree_node, p) -> list:
    # does a pre-order traversal; would be faster with an accumulator list
    lst = list()
    (data, children) = tree_node
    if p(data):
        lst.append(data)
    
    for child_node in children:
        lst.extend(filter_tree(child_node, p))
    return lst

print("1.4.c")
print(filter_tree(files, lambda filename: filename.endswith(".jpg")))

# 1.4.d

# this algorithm does a depth-first search in the tree graph
def find_node_path(tree_node:tuple, path:list) -> tuple:
    # path mismatch
    if len(path) == 0:
        return None
    
    (name, children) = tree_node
    if name == path[0]:              # match file or directory name
        if len(path) == 1:
            return tree_node  # found the right node to return
        
        # keep looking in subdirectories:
        for child in children:
            found_node = find_node_path(child, path[1:])
            if found_node != None:
                return found_node
    return None

print("\n1.4.d\n")
node1 = find_node_path(files, ["/", "home", "bob", "photos", "pic1.jpg"])
print(node1)

node2 = find_node_path(files, ["/", "home", "bob", "photos", "nosuchfile.jpg"])
print(node2)

node3 = find_node_path(files, ["/", "home", "ana", "photos"])
print(node3)

node4 = find_node_path(files, ["/", "home", "santa", "gifts"])
print(node4)



# 1.5
def s_m(n):
    """
    1.5 
    Write a memoized version for the recursive function that produces 
    a famous number series starting with 
    0, 1, and then numbers s(n), with s(n) = 2 * s(n - 1) - s(n - 2).
    What do you notice?
"""  
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 2*s_m(n-1) - s_m(n-2)
        


def series(n:int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 2 * series(n - 1) - series(n - 2)


def series_m(n:int, hist=dict()):
    if n in hist:
        return hist[n]
    r = 0
    if n == 1:
        r = 1
    elif n > 1:
        r = 2 * series_m(n - 1) - series_m(n - 2)
    hist[n] = r
    return r

print("\n\n1.5 - Memoization")
print([series(i) for i in range(10)])
print([series_m(i) for i in range(10)])




# ===================================================

# 2.1
# this class is an iterable and also an iterator
class Parselines:
    def __init__(self, text:str):
        self._text = text
        
        # this attribute remembers the starting position of the next line:
        self._index = 0
    
    # return this object that is also an iterator
    def __iter__(self):
        return self
    
    def __next__(self):
        # are we at the end of the line?
        if self._index >= len(self._text):
            raise StopIteration()
            
        line_end_pos = self._text.find("\n", self._index)
        if line_end_pos == -1:       # newline not found
            pos = len(self._text)    # mark the end of the text reached
            nextindex = pos
        else:
            pos = line_end_pos
            nextindex = pos + 1    # don't return \n
        s = self._text[self._index:pos]
        self._index = nextindex
        return s
        
print("\n\n2.1") 
text = "First line.\nSecond line.\n\n  Third line with spaces.\n"
lp = Parselines(text)
for (i, line) in enumerate(lp):
    print(f"line {i}: {line}")
    

# 2.2

# This solution uses an inner class, but that is just an optional design choice.
class Parselines2:
    def __init__(self, text:str):
        self._text = text
        
        # this attribute remembers the starting position of the next line:        
        
    class LineIterator:
        def __init__(self, text:str):
            self._text = text
            self._index = 0
        
        def __next__(self):
            # are we at the end of the line?
            if self._index >= len(self._text):
                raise StopIteration()
                
            line_end_pos = self._text.find("\n", self._index)
            if line_end_pos == -1:       # newline not found
                pos = len(self._text)    # mark the end of the text reached
                nextindex = pos
            else:
                pos = line_end_pos
                nextindex = pos + 1
            s = self._text[self._index:pos]
            self._index = nextindex
            return s

    # __iter__ is defined for class Parselines2:
    def __iter__(self):
        return Parselines2.LineIterator(self._text)
            
        
print("\n\n2.2") 
text = "First line.\nSecond line.\n\n  Third line with spaces.\n"
lp = Parselines2(text)
for (i, line) in enumerate(lp):
    print(f"line {i}: {line}")
    
# ============================================================================    

# --------------------
# We need these:

def gen_infinite_fibonacci(f0=0, f1=1):
    while True:
        yield f0
        f0, f1 = f1, f0+f1

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
    
# --------------------    

# 3.1
"""
Write a generator concat(it1, it2) that generates the sequence of objects from
iterable it1 followed by the sequence of objects from iterable it2.

Write some code that demonstrates how to use concat.
"""



def concat(it1, it2):
    for x in it1:
        yield x

    for y in it2:
        yield y

print("\n\n3.1\n") 
print(list(concat(range(4), range(10, 16))))


# 3.2

def gen_enumerate(seq):
    i = 0
    for x in seq:
        yield (i, x)
        i += 1

print("\n\n3.2\n") 
print(list(gen_enumerate("abcdefg")))


# 3.3
print("\n\n3.3\n")

n = 1000000

# we need the first (take_n(1,....)) tuple of a stream of numbers >= n.
# Apply take_n(1, gen_fiter( ... to a sequence of tuples (0, f0), (1, f1),...
# where the fs are Fib. numbers.
# the filter then applies to (i, fi) tuples.
fib_tuple = next(take_n(1, 
                        gen_filter(lambda i_fibi: i_fibi[1] >= n, 
                                   gen_enumerate(
                                       gen_infinite_fibonacci()))))
print(fib_tuple)


# 3.4

def concat2(*iterables):    
    # iterables is a tuple with iterable sequences
    for seq in iterables:
        for x in seq:
            yield x

# show concatenation of list with a tuple with a string and a set:

print("\n\n3.4\n")
print(list(concat2([1,2,3], (10, 20), "abcd", {200, 100})))       


# 3.5

def file_words(filename:str):
    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                yield word

# prepare a file:
filename = "_sometext.txt"     
with open(filename, "w") as f:
    f.write(
"""
Four score and seven years ago our
fathers brought forth on this continent, a new nation, 
conceived in Liberty, and dedicated to the proposition 
that all men are created equal.
""")

print("\n\n3.5\n")
print(list(file_words(filename))[:10])
      
# =============================================================================

# 4.1

print("\n\n4.1\n")
lst = [10, 5, 11, 4, 4, 7]
seq = (f"select {n}" for n in lst if n >= 10)
print("4.1 as list:", list(seq))


# 4.2
lst1 = [4, 3, 5, 1, 6]
lst2 = [6, 2, 3]
seq = ((i, j) for i in lst1 for j in lst2 if i < j)
print("4.2 as list:", list(seq))

# =============================================================================


print("\n\n5.1\n")

#students = [("Alice", 80), ("Bob", 85), ("Eve", 67), ("Fred", 75), ("Jose", 90)]

car_ads = [("Civic EX", "Honda", 12000), ("Cherokee", "Jeep", 9000),
           ("Prelude", "Honda", 10000), ("Patriot", "Jeep", 8000)]
 
cars = filter(lambda ad: ad[1] == "Honda", car_ads)
prices = map(lambda ad: ad[2], cars)     # get just the price from each tuple

# prices is a sequence of numbers (for Honda ads)
# For an average we need the count of numbers and their sum.

# We don't know ahead of time how many numbers there are -- we work with iterables,
# not necessarily lists. Use reduce to keep a running (partial_count, partial_sum).

# the function argument to reduce has two arguments: f(x, y) where
# x is the partial result and y is the current element from the sequence.
# (0, 0.0) is (initial_count, initial_sum)
price_count_sum = functools.reduce(lambda c_s, p: (c_s[0] + 1, c_s[1] + p), prices, (0, 0.0))
average_price = price_count_sum[1] / price_count_sum[0]
# we did  not check for /0 error....
print("\n\n5.1 FILTER, MAP, REDUCE")
print(f"average price for Hondas in f{car_ads} is {average_price}\n")


# 6.1
def trace_fun(f):
    def wrapper(x):
        print(f"Calling {f.__name__}({x})...")
        y = f(x)
        print("    --- result is", y)
        return y
    return wrapper

# decorating a sample function inc:
@trace_fun    
def inc(x):
    return x + 1 

print("\n\n6.1 Decorator for inc:")

z = inc(10)   # calls the wrapper instead and prints tracing info


# 7.1
print("\n\n7.1\n")

A = np.arange(12).reshape((3,4))
print(A)

A[1:, 2:] = 0
print(A)

A[A==0]=-1
print(A)

# 7.2
n = 50    # number of points
K = 3.0   # interval for x and y: [-K, K]    
B = np.fromfunction(lambda i, j: (2 * K * i/n - K)**2 + (2 * K * j / n - K)**2, (n, n))

plt.imshow(B, cmap='plasma', interpolation='none')
plt.colorbar()
plt.show()
