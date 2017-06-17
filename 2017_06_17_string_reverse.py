"""
Question:

Reverse a string without using any built in functions.
Input: Hello
Output: olleH
"""

def reverse_me(string):
    """
    Theory
    """
    result = ''
    for s in string:
        result = s + result
    return result


def main():
    string = raw_input("Provide the string to reverse?: ")
    print reverse_me(string)


if __name__ == '__main__':
    main()
