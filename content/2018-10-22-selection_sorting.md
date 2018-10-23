Category: Algorithm
Tags: Python

Selection sorting is an in-place sort algorithm. The idea is selecting the min/max element and swap it with the first element in the unsorted side. In other words, it appends the correct element from the unsorted side to the sorted side. The sorting repeats this until no element is left on the unsorted side.

The characteristics and performance of the sorting include:

* Space Complexity: O(1)
* Non-stability
* Worst-case Time Complexity: O(n^2) comparison and O(n) swapping
* Best-case Time Complexity: O(n^2) comparison and O(1) swapping

The implementation in Python is as follow:

```python
def selection_sort(elements):
    for i in range(len(elements)):
        max_index = i
        max_element = elements[i]

        for index, element in enumerate(elements[i:]):
            if element < max_element:
                max_index = i + index
                max_element = element

        if max_index != i:
            swap(elements, max_index, i)
```
