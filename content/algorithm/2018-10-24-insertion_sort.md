Tags: python
Status: draft

The idea of insertion sort is moving the first element on the unsorted side, one by one, toward the start of the sorted side, until it is adjacent to a smaller element. The sort repeats this, each time reducing the unsorted side by 1 element, until all elements are moved.

Each loop actually moves an element on the unsorted side to its correct position on the sorted side.

- Space Complexity of O(1):

No additional list is used.

- Stability:

The sort only swaps adjacent, unequal elements so the relative order of equal elements are not broken.

- Worst-case Time Complexity of O(n^2) Comparison and O(n^2) Swapping:

In the worst case, the sort has n loops, with each loop having n-depended comparisons and n-depended swappings.

- Implementation in Python:

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
