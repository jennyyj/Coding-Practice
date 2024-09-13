# (a) Mstring class

class Mstring:
    def __init__(self, obj):
        self._characters = list(str(obj))

    def __len__(self):
        return len(self._characters)

    def __str__(self):
        return ''.join(self._characters)

    def __repr__(self):
        return ''.join(self._characters)

    def __add__(self, other):
        if isinstance(other, Mstring):
            return Mstring(self._characters + other._characters)
        else:
            return Mstring(self._characters + list(str(other)))

    def __radd__(self, other):
        return Mstring(list(str(other)) + self._characters)

    def __getitem__(self, index):
        return self._characters[index]

    def __setitem__(self, index, value):
        if not isinstance(value, str) or len(value) != 1:
            raise ValueError("Invalid value, must be a single character")
        self._characters[index] = value

    def __eq__(self, other):
        return ''.join(self._characters) == str(other)

    def __ne__(self, other):
        return ''.join(self._characters) != str(other)

    def replace(self, s, t):
        string_repr = ''.join(self._characters)
        index = string_repr.find(s)
        if index != -1:
            self._characters = list(string_repr.replace(s, t, 1))
        return index

    def find(self, s):
        return ''.join(self._characters).find(s)



# (b) Test functions

def testif(test_result, description):
    """Prints the description along with the result of the test."""
    if test_result:
        print(f"PASS: {description}")
    else:
        print(f"FAIL: {description}")

def unit_tests():
    # Test __eq__
    test1 = Mstring("abcd")
    test2 = Mstring("abcd")
    testif(test1 == test2, "Test __eq__ passed")
    testif(not test1 != test2, "Test __ne__ passed")

    # Test __ne__
    test3 = Mstring("abcd")
    test4 = Mstring("abcX")
    testif(test3 != test4, "Test __ne__ passed")
    testif(not test3 == test4, "Test __eq__ passed")

    # Test __str__
    test5 = Mstring("Hello World")
    testif(str(test5) == "Hello World", "Test __str__ passed")

    # Test __len__
    test6 = Mstring("Hello World")
    testif(len(test6) == 11, "Test __len__ passed")
    testif(len(Mstring("")) == 0, "Test __len__ for empty string passed")

    # Test __add__
    test7 = Mstring("abcdef")
    test8 = Mstring("1234")
    testif((test7 + test8).__str__() == "abcdef1234", "Test __add__ passed")
    testif((Mstring("") + test7).__str__() == "abcdef", "Test __add__ with empty string passed")

    # Test __radd__
    test9 = Mstring("abcdef")
    result = "1234" + test9
    testif(result.__str__() == "1234abcdef", "Test __radd__ passed")
    testif((test9 + "").__str__() == "abcdef", "Test __radd__ with empty string passed")

    # Test __setitem__
    test10 = Mstring("abcdef")
    test10[2] = "X"
    testif(test10.__str__() == "abXdef", "Test __setitem__ passed")

    try:
        test10[7] = "Y"  # throws index error
        testif(False, "Test __setitem__ failed (IndexError not raised)")
    except IndexError:
        testif(True, "Test __setitem__ passed (IndexError raised)")

    # Test __getitem__
    test11 = Mstring("abcdef")
    testif(test11[2] == "c", "Test __getitem__ passed")
    testif(test11[-1] == "f", "Test __getitem__ with negative index passed")

    try:
        test11[20]  # throws IndexError
        testif(False, "Test __getitem__ failed (IndexError not raised)")
    except IndexError:
        testif(True, "Test __getitem__ passed (IndexError raised)")

    # Test replace
    test_replace = Mstring("abcdeabcde")
    testif(test_replace.replace("abc", "XYZ") == 0, "Test replace passed")
    testif(test_replace.__str__() == "XYZdeabcde", "Test replace passed")

    # Test find
    test_find = Mstring("01234567")
    testif(test_find.find("45") == 4, "Test find passed")
    testif(test_find.find("abc") == -1, "Test find passed")

# (c) Quicksort 

def quicksort(mstring):
    if len(mstring) <= 1:
        return mstring
    else:
        pivot = mstring[0]
        less = quicksort(Mstring([c for c in mstring[1:] if c < pivot]))
        equal = Mstring([c for c in mstring if c == pivot])
        greater = quicksort(Mstring([c for c in mstring[1:] if c > pivot]))
        return less + equal + greater

# (d) Test Sorting 

def test_sort():
    # Test quicksort on Mstring objects
    test12 = Mstring("cba")
    sorted_test12 = quicksort(test12)
    testif(sorted_test12.__str__() == "abc", "Test quicksort passed")

    # Test quicksort on an empty Mstring
    test13 = Mstring("")
    sorted_test13 = quicksort(test13)
    testif(sorted_test13.__str__() == "", "Test quicksort passed")

    # Additional tests
    test14 = Mstring("zyx")
    sorted_test14 = quicksort(test14)
    testif(sorted_test14.__str__() == "xyz", "Test quicksort passed")

    test15 = Mstring("hello")
    sorted_test15 = quicksort(test15)
    testif(sorted_test15.__str__() == "ehllo", "Test quicksort passed")

    print("Sorting tests passed successfully!")

# (e) Mains

def main():
    unit_tests()
    test_sort()

if __name__ == "__main__":
    main()