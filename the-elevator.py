from typing import List

def elevator(floors: int, passengers: List[int, int], max_capacity: int) -> List[int]:
    """
    Rules:
    The elevator starts on floor 1.
    Each passenger starts on a floor pf1 (1 < pf1 < F)
    Their destination is floor pf2 (1 < pf2 < F)
    What is the most efficient way that the elevator can transport people
    to their respective locations, given a max capacity?
    Return a list of floors visited, including the starting floor

    Example:
    elevator(5, [[1, 2], [3, 4], [5, 1], [1, 4]], 2)\n
    |-------------|\n
    |  1          | - 5\n
    |-------------|\n
    |             | - 4\n
    |-------------|\n
    |  4          | - 3\n
    |-------------|\n
    |             | - 2\n
    |-------------|\n
    |  2  4  ELV  | - 1\n
    |-------------|\n

    Return: [1, 2, 3, 4, 5, 1]


    :param floors: int
    :param passengers: list[int]
    :return:
    """
    pass