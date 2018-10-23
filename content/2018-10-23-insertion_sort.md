Category: Algorithm
Tags: Python

The idea of insertion sorting is inserting each element from the unsorted side to its correct position on the sorted side. This is done by repeatedly swapping the element with its adjacent element toward the sorted side. The sorting repeats this until no element is left on the unsorted side.

The characteristics and performance of the sorting include:

* Space Complexity: O(1)
* Stability
* Worst-case Time Complexity: O(n^2) comparison and O(n^2) swapping
* Best-case Time Complexity: O(n) comparison and O(1) swapping

The implementation in Python is:

```python
def swap(elements, index_1, index_2):
    elements[index_1], elements[index_2] = elements[index_2], elements[index_1]

def insertion_sort(elements):
    for i in range(len(elements)):
        for index in reversed(range(i)):
            if elements[index+1] < elements[index]:
                swap(elements, index+1, index)
            else:
                break
```
