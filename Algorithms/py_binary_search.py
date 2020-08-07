def py_binary_search(arr, val):
    leftBound = 0
    rightBound = len(arr)
    
    while leftBound <= rightBound:
        mid = (leftBound + rightBound) / 2
        if arr[mid] == val:
            return mid
        elif val > arr[mid]:
            leftBound = mid + 1
        else:
            rightBound = mid - 1
        
    return -1
