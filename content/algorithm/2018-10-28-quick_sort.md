Tags: Python

The idea of quick sort is choosing one element as the pivot and divide the others into two lists, one with larger and one with smaller elements than the pivot. This is done by selecting, from the two ends of the list and toward the middle, elements which are on incorrect sides and swapping them, until the two selections meet each others. The sort repeats this until the sub-lists only have one element and cannot be divided anymore.

\- Space Complexity of O(1):

The sort is in-place, which means only swapping elements in the list.

\- Non-stability:

When swapping elements to divide them into sub-lists, equal elements on the same incorrect side are reversed in order after swapped, as the two selections move from the two ends of the list toward the middle.

\- Worst-case Time Complexity of O(n^2) Comparison and O(n^2) Swapping:

The case happens when each dividing has the largest/smallest element as the pivot and the rest are on their incorrect side, and thus produces one empty sub-list and another sub-list with the remaining elements. This leads to n dividing, with each dividing having 2n comparison from one selection and 0 comparision from the other selection, as well as n swappings.

\- Implementation in Python:

```python
def swap(elements, index_1, index_2):
    elements[index_1], elements[index_2] = elements[index_2], elements[index_1]

def quick_sort(elements):

    def recurse(elements, start_index, end_index):
        if start_index < end_index - 1:
            pivot_index = partition(elements, start_index, end_index)
            recurse(elements, start_index, pivot_index)
            recurse(elements, pivot_index+1, end_index)

    # dividing
    def partition(elements, start_index, end_index):
        pivot = elements[start_index]
        left_i = start_index
        right_i = end_index - 1

        while True:
            # selection from the start
            while elements[left_i] <= pivot:
                left_i += 1
                if left_i == end_index - 1:
                    break

            # selection from the end
            while elements[right_i] >= pivot:
                right_i -= 1
                if right_i == start_index:
                    break

            if left_i >= right_i:
                swap(elements, start_index, right_i)
                return right_i
            swap(elements, left_i, right_i)

    recurse(elements, 0, len(elements))
```
