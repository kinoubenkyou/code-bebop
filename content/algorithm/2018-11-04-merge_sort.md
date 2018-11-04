Tags: Python

The idea of merge sort is merging two sub-lists of equal length into one sorted list. This is done by copying the larger/smaller between the largest/smallest elements, which have not been copied, on the two sub-lists. The sub-lists are sorted themselves through the same merging of their own sub-lists. The smallest sub-lists are the one-element sub-lists.

\- Space Complexity of O(n):

The sort uses another array to store the result of the merging before copying back to the list, and thus uses an array with length of n in the last merging.

\- Stability:

When merging equal elements are copied in their relative order.

\- Worst-case Time Complexity of O(nlogn) Comparison and O(nlogn) Swapping:

The sort always has logn merging. The case happens when each merging has both sub-lists take turn in having their elements copied, and thus has n comparisons as well as n copyings.

\- Implementation in Python:

```python
def swap(elements, index_1, index_2):
    elements[index_1], elements[index_2] = elements[index_2], elements[index_1]


def merge_sort(elements):

    def recurse(elements, start_index, end_index):
        if end_index - start_index > 1:
            sep_index = (end_index - start_index) // 2 + start_index
            recurse(elements, start_index, sep_index)
            recurse(elements, sep_index, end_index)
            merge(elements, start_index, end_index, sep_index)

    def merge(elements, start_index, end_index, sep_index):
        left_i = start_index
        right_i = sep_index
        merged_elements = []

        while True:
            if left_i >= sep_index:
                merged_elements.extend(elements[right_i:end_index])
                break
            if right_i >= end_index:
                merged_elements.extend(elements[left_i:sep_index])
                break

            if elements[left_i] > elements[right_i]:
                merged_elements.append(elements[right_i])
                right_i += 1
            else:
                merged_elements.append(elements[left_i])
                left_i += 1

        elements[start_index:end_index] = merged_elements

    recurse(elements, 0, len(elements))
```
