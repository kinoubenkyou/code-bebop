Category: Algorithm
Tags: Python

The idea bubble sort is comparing each pair of adjacent elements and swapping them if they are in the wrong order. This does not only prepends the largest/smallest element to the sorted side, but also partially moves other elements toward their correct position. The sort repeats this until no element is left on the unsorted side.

\- Space Complexity of O(1):

The sort is in-place, which means only swapping elements in the list.

\- Stability:

The sort only swaps adjacent, unequal elements so the order of equal elements are not broken.

\- Worst-case Time Complexity of O(n^2) Comparison and O(n^2) Swapping:

The case happens when all loops of prepending to the sorted side have every pair of adjacent elements swapped. This leads to n loops of prepending, with each loop having n comparisons for pair of adjacent elements, as well as n swappings.

\- Best-case Time Complexity of O(n) Comparison and O(1) Swapping:

The case happens when the first loop of prepending to the sorted side have no swapping, so the sort stop early. This leads to only 1 loop of prepending, with n comparisons for pair of adjacent elements, as well as 0 swappings.

\- Implementation in Python:

```python
def swap(elements, index_1, index_2):
    elements[index_1], elements[index_2] = elements[index_2], elements[index_1]

def bubble_sort(elements):
    # loop of prepending to the sorted side
    for i in range(len(elements)):
        did_swap = False
        for index in reversed(range(i+1, len(elements))):
            if elements[index] < elements[index-1]:
                swap(elements, index, index-1)
                did_swap = True

        if not did_swap:
            break
```
