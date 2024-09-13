def find_dup_str(s, n):
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        rest_of_string = s[i+n:]
        if substring in rest_of_string:
            return substring
    return ""

# Testing the function
if __name__ == "__main__":
    s_input = input("Enter a string: ")
    n_input = int(input("Enter the length of the substring to check for duplication: "))

    result = find_dup_str(s_input, n_input)
    print(f"Result for find_dup_str: {result}")

def find_max_dup(s):
    max_length = 0
    max_duplicate = ""

    for length in range(1, len(s)):
        duplicate = find_dup_str(s, length)
        if duplicate:
            max_length = length
            max_duplicate = duplicate

    return max_duplicate

# Testing find_max_dup
if __name__ == "__main__":
    s_input_b = input("Enter a string for find_max_dup: ")
    
    result_b = find_max_dup(s_input_b)
    print(f"Result for find_max_dup: {result_b}")
