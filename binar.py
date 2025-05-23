def binary_search(num, x):
    left = 0
    right = len(num) - 1
    while left <= right:
        mid = (left + right) // 2
        if num[mid]==x:
            return mid
        elif num[mid]<x:
            left = mid+1
        else:
            right = mid-1
    return -1
print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 6))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 8))