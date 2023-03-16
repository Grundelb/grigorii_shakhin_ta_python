"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    '''
    If there's only one list, the function returns a list of lists, where each inner list contains one item from the input list.
    If there are more than one list, the function recursively calls itself with all but the first list as arguments. 
    This returns a list of all possible combinations of the remaining lists.
    For each item in the first list, the function iterates over the list of all possible combinations of the remaining lists, 
    and appends a new list that starts with the current item to each combination.
    The function returns the list of all combinations.
    '''
    if len(args) == 1:
        return [[item] for item in args[0]]
    else:
        result = []
        for item in args[0]:
            for sublist in combinations(*args[1:]):
                result.append([item] + sublist)
        return result
