Tags: python, algorithm

# Idea:

Bubble sort compares each pair of adjacent elements on the unsorted side of the list and swapping them if they are in the wrong order. The sort repeats this, each time reducing the unsorted side by 1 element at the end, until no element is left on the unsorted side.

Each loop moves the largest element on the unsorted side, one by one element, to the sorted side. It also partially moves other elements toward the sorted side.

# Space Complexity of O(1):

No additional list is used.

# Stability:

The sort only swaps adjacent, unequal elements so the relative order of equal elements are not broken.

# Worst-case Time Complexity of O(n^2) Comparison and O(n^2) Swapping:

In the worst case, the sort has n loops, with each loop having n-depended comparisions and n-depended swappings.

# Implementation in Python:

```python
def swap(elements, index_1, index_2):
    elements[index_1], elements[index_2] = elements[index_2], elements[index_1]

def bubble_sort(elements):
    for i in range(len(elements)):
        did_swap = False
        for index in range(len(elements) - 2 - i):
            if elements[index] > elements[index+1]:
                swap(elements, index, index+1)
                did_swap = True

        if not did_swap:
            break
```
