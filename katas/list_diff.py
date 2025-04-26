def find_difference(numbers):
    """
    Finds the difference between the largest and smallest numbers in the list.

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers

    """
    min_number = numbers[0]
    max_number = numbers[0]
    for num in numbers:
        if num < min_number :
            min_number =  num
        if num > max_number :
            max_number = num

    return max_number - min_number


if __name__ == '__main__':
    sample_list = [10, 3, 5, 6, 20, -2]
    difference = find_difference(sample_list)
    print(difference)  # 22 should be printed