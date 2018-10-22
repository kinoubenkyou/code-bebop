Category: Algorithm
Tags: Python

The idea for selection sorting is selecting the min/max element and swap it with the first element in the unsorted side. The characteristics and performance of the sorting include:

* Space complexity of O(1): the sorting involves swaping only elements on the list.
* Non-stability: the sorting changes the position of elements in the unsorted side when it does the swapping.
* Worst-case time complexity of O(n^2) comparison and O(n) swapping: the sorting involves 2 levels of looping.
* Best-case time complexity of O(n^2) comparison and O(1) swapping: if the list is already sorted, no swapping will happen but all the comparison will remain.

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
