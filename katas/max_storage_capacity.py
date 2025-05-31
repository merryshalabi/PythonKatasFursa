from typing import List


def max_storage_area(containers: List[int]) -> int:
    """
    Imagine a series of storage containers placed side by side, where the height of each container
    is given by an integer in the array. Your task is to find the largest rectangular area that
    can be formed using one or more of these containers.

    For example:
    Input: containers = [2, 1, 5, 6, 2, 3]
    Output: 10
    Explanation: The largest rectangle is formed between containers at indices 2 and 3
    with height 5 and width 2.

    Hint for efficient implementation: stack

    Args:
        containers: a list of integers representing the heights of containers

    Returns:
        The area of the largest rectangle formed between containers
    """
    containers = containers.copy()
    containers.append(0)

    stack = []
    max_area = 0

    for i in range(len(containers)):
        current_height = containers[i]


        while stack and containers[stack[-1]] > current_height:
            top_index = stack.pop()
            height = containers[top_index]


            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            area = height * width
            max_area = max(max_area, area)


        stack.append(i)

    return max_area



if __name__ == "__main__":
    containers = [2, 1, 5, 6, 2, 3]
    result = max_storage_area(containers)
    print("Max storage area:", result)  # Expected output: 10
