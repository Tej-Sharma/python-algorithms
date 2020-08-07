def py_quicksort(arr):
    left = []
    middle = []
    right = []
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) - 1]
        for i in arr:
            if i > pivot:
                right.append(i)
            elif i < pivot:
                left.append(i)
            else:
                middle.append(pivot)
        # Now divide and conquer
        return py_quicksort(left) + middle + py_quicksort(right)
        
test = [15, 25, 1337, 5, 69, 200, 420]

print (py_quicksort(test))
