Category: Algorithm
Tags: Python

The idea bubble sorting is comparing each pair of adjacent elements and swapping them if they are in the wrong order. This does not only appends the min/max element to the sorted side, but also partially moves other elements toward their correct position. The sorting repeats this until no element is left on the unsorted side.

The characteristics and performance of the sorting include:

* Space Complexity: O(1)
* Stability
* Worst-case Time Complexity: O(n^2) comparison and O(n^2) swapping
* Best-case Time Complexity: O(n) comparison and O(1) swapping

The implementation in Python is:

```python
def swap(elements, index_1, index_2):
    elements[index_1], elements[index_2] = elements[index_2], elements[index_1]

def bubble_sort(elements):
    for i in range(len(elements)):
        did_swap = False
        for index in reversed(range(i+1, len(elements))):
            if elements[index] < elements[index-1]:
                swap(elements, index, index-1)
                did_swap = True

        if not did_swap:
            break
```
