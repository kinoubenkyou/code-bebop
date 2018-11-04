Tags: Python

The idea bubble sort is comparing each pair of adjacent elements and swapping them if they are in the wrong order. This does not only ultimately prepends the largest/smallest element to the sorted side, but also partially moves other elements toward their correct position. The sort repeats this until no element is left on the unsorted side.

\- Space Complexity of O(1):

The sort is in-place, which means only swapping elements in the list.

\- Stability:

The sort only swaps adjacent, unequal elements so the order of equal elements are not broken.

\- Worst-case Time Complexity of O(n^2) Comparison and O(n^2) Swapping:

This case happens when the list is sorted in the reversed direction and thus all loops of swapping round have every pair of adjacent elements swapped. This leads to n loops of swapping round, with each loop having n comparisons and n swappings of adjacent element's pair.

\- Implementation in Python:

```python
def swap(elements, index_1, index_2):
    elements[index_1], elements[index_2] = elements[index_2], elements[index_1]

def bubble_sort(elements):
    # loop of swapping round
    for i in range(len(elements)):
        did_swap = False
        for index in reversed(range(i+1, len(elements))):
            if elements[index] < elements[index-1]:
                swap(elements, index, index-1)
                did_swap = True

        if not did_swap:
            break
```
