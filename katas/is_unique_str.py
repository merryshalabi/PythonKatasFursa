def is_unique(string):
    """
    Checks if a string has all unique characters (case-insensitive).

    Args:
        string: the input string

    Returns:
        True if all characters are unique, False otherwise
    """
    alphabet_counter = [0] * 26
    for letter in string:
        letter = letter.lower()
        if not letter.isalpha():
            continue
        index = ord(letter) - ord('a')
        if alphabet_counter[index] :
             return False
        alphabet_counter[index]+=1

    return True


if __name__ == '__main__':
    test1 = "Hello"
    test2 = "World"
    test3 = "Python"
    test4 = "Unique"

    print(f'"{test1}" has all unique characters: {is_unique(test1)}')  # Should be False (has repeated 'l')
    print(f'"{test2}" has all unique characters: {is_unique(test2)}')  # Should be True
    print(f'"{test3}" has all unique characters: {is_unique(test3)}')  # Should be True
    print(f'"{test4}" has all unique characters: {is_unique(test4)}')  # Should be True