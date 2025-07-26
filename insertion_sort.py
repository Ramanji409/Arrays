def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1

        # Move numbers greater than key to one position right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift element
            j -= 1

        # Place the key at its correct position
        arr[j + 1] = key

    return arr

# Example usage
numbers = [29, 10, 14, 37, 13]
sorted_numbers = insertion_sort(numbers)
print("Sorted array:", sorted_numbers)