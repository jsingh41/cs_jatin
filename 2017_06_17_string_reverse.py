"""
Question:

Reverse a string without using any built in functions.
Input: Hello
Output: olleH
"""

def reverse_1(string):
    """
    Using for loop
    """
    result = ''
    for s in string:
        result = s + result
    return result


def reverse_2(string):
    # Using Python's function
    # in string[start:end:increment by]
    return string[::-1]


def reverse_3(string):
    # Using while loop
    index = len(string) - 1
    result = ''
    while index >= 0:
        result = result + string[index]
        index = index - 1
    return result


def main():
    string = raw_input("Provide the string to reverse?: ")
    print reverse_1(string)
    print reverse_2(string)
    print reverse_3(string)


if __name__ == '__main__':
    main()
