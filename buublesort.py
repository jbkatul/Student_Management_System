def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize the algorithm by checking if any swaps occurred in this iteration
        swapped = False

        # Last i elements are already sorted, so no need to check them again
        for j in range(0, n-i-1):
            # If the element at j is greater than the element at j+1, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped in this iteration, the list is already sorted
        if not swapped:
            break

# Example usage:
if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original List:", my_list)
    bubble_sort(my_list)
    print("Sorted List:", my_list)
