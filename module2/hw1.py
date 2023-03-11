"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp:List) -> Tuple[int, int]:
    candidate, count = None, 0
    for x in inp:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1
    most_common = candidate
    
    freq = {}
    for x in inp:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    least_common = list(freq.keys())[list(freq.values()).index(min(freq.values()))]
    
    return most_common, least_common