def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle +1
        return middle


x = binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5)
print(x)