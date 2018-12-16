Tags: python 

The idea of selection sort is finding the smallest element on the unsorted side of the list and swap it with the first element on the unsorted side. The sort repeats this, each time reducing the unsorted side by 1 element, until all elements are swapped.

Each loop actually finds and appends the smallest element on the unsorted to the sorted side.

- Space Complexity of O(1):

No additional list is used.

- Non-stability:

When swapping, selection sort breaks the relative order between equal elements.

- Worst-case Time Complexity of O(n^2) Comparison and O(n) Swapping:

In the worst case, the sort has n loops, with each loop having n-depended comparisons and 1 swapping.

- Implementation in Python:

```python
def swap(elements, index_1, index_2):
    elements[index_1], elements[index_2] = elements[index_2], elements[index_1]

def selection_sort(elements):
    for i in range(len(elements)):
        min_index = i
        min_element = elements[i]

        for index in range(i+1, len(elements)):
            if elements[index] < min_element:
                min_index = index
                min_element = elements[index]

        if min_index != i:
            print(min_index, i)
            swap(elements, min_index, i)
```
