def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Get input from user
user_input = input("Enter numbers separated by spaces: ")
# Convert the input string into a list of integers
data = [int(x) for x in user_input.split()]

print("Sorted list:", bubble_sort(data))