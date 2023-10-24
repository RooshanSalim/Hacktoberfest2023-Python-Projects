def merge_sort(array):
  """Sorts an array using the merge sort algorithm.

  Args:
    array: An array to be sorted.

  Returns:
    A sorted array.
  """

  # If the array is empty or has only one element, it is already sorted.
  if len(array) <= 1:
    return array

  # Divide the array into two halves.
  mid = len(array) // 2
  left = merge_sort(array[:mid])
  right = merge_sort(array[mid:])

  # Merge the two sorted halves.
  return merge(left, right)


def merge(left, right):
  """Merges two sorted arrays into a single sorted array.

  Args:
    left: A sorted array.
    right: A sorted array.

  Returns:
    A sorted array containing all the elements of the two input arrays.
  """

  result = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  # Add any remaining elements from the left and right arrays.
  result += left[i:]
  result += right[j:]

  return result


# Example usage:

array = [5, 3, 2, 1, 4]

sorted_array = merge_sort(array)

print(sorted_array)
