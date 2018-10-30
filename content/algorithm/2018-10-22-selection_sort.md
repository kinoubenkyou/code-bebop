Category: Algorithm
Tags: Python

The idea of selection sort is selecting the largest/smallest element and swap it with the first element on the unsorted side on the list. In other words, it appends the correct element from the unsorted side to the sorted side. The sort repeats this until no element is left on the unsorted side.

\- Space Complexity of O(1):

The sort is in-place, which means only swapping elements in the list.

\- Non-stability:

When swapping with the first element on the unsorted side, the element's order relative to its other equal elements might be broken.

\- Worst-case Time Complexity of O(n^2) Comparison and O(n) Swapping:

The sort always has n loops of finding the largest/smallest element, and each loop has n comparisons. This case happens when the list is sorted in the reversed direction and thus all loops have swapping.

\- Best-case Time Complexity of O(n^2) Comparison and O(1) Swapping:

The sort always has n^2 comparisons as explained in the worst case. This case happens when the list is already sorted and thus all loops have no swapping.

\- Implementation in Python:

```python
def swap(elements, index_1, index_2):
    elements[index_1], elements[index_2] = elements[index_2], elements[index_1]

def selection_sort(elements):
    # loops of finding largest element
    for i in range(len(elements)):
        max_index = i
        max_element = elements[i]

        for index, element in enumerate(elements[i:]):
            if element < max_element:
                max_index = i + index
                max_element = element

        # swapping the largest element with the first element on the unsorted side
        if max_index != i:
            swap(elements, max_index, i)
```
