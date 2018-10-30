Category: Algorithm
Tags: Python

The idea of insertion sort is inserting each element from the unsorted side to its correct position on the sorted side. This is done by repeatedly swapping the element with its adjacent element toward the sorted side. The sort repeats this until no element is left on the unsorted side.

The characteristics and performance of the sort include:


\- Space Complexity of O(1):

The sort is in-place, which means only swapping elements in the list.

\- Stability:

The sort only swaps adjacent, unequal elements so the order of equal elements are not broken.

\- Worst-case Time Complexity of O(n^2) Comparison and O(n^2) Swapping:

This case happens when the list is sorted in the reversed direction and thus all loops of inserting have the first element on the unsorted swapped until it reachs the end of the sorted side. This leads to n loops of inserting, with each loop having n comparisons and n swappings of adjacent element's pair.

\- Best-case Time Complexity of O(n) Comparison and O(1) Swapping:

This case happens when the list is sorted in the reversed direction and thus all loops of inserting stop at their first comparison. This leads to n loops of inserting, with each loop having only 1 comparison and 0 swapping of adjacent element's pair.

\- Implementation in Python:

```python
def swap(elements, index_1, index_2):
    elements[index_1], elements[index_2] = elements[index_2], elements[index_1]

def insertion_sort(elements):
    # loop of inserting
    for i in range(len(elements)):
        for index in reversed(range(i)):
            if elements[index+1] < elements[index]:
                swap(elements, index+1, index)
            else:
                break
```
