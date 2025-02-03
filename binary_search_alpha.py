def binary_search(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return -1

if __name__ == "__main__":
    arr = ['a', 'b', 'c', 'e', 'd', 'f', 'g']
    target = 'e'

    
    arr.sort()

    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print(f"Element not found in the array")
