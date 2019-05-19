Tags: python, algorithm

# Idea:

Quick sort chooses one element as the pivot and separates the others into two lists, one with larger and one with smaller elements than the pivot. This is done by, from the two ends of the list toward the middle, selecting elements which are on incorrect sides and swapping them, until the two selections meet each others. The sort repeats this on the two sub-lists until the they only have one element and cannot be divided anymore.

# Space Complexity of O(1):

No additional list is used.

# Non-stability:

When swapping elements to divide them into sub-lists, equal elements on the same incorrect side are reversed in order after being swapped, as the selection move from the two ends of the list toward the middle.

# Worst-case Time Complexity of O(n^2) Comparison and O(n^2) Swapping:

In the worst case, the sort has n recursions since each recursion having the largest/smallest element as the pivot and the rest are on their incorrect side. Thus, each recursion has n-depended comparisons and n-depended swappings.

# Implementation in Python:

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
            while elements[left_i] <= pivot:
                left_i += 1
                if left_i == end_index - 1:
                    break

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
