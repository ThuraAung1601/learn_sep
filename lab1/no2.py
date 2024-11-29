def BSearch(num, arr, low, high):
    if(low > high):
        return -1
    mid = low + int((high - low)/2)
    if num == arr[mid]:
        return mid
    elif num < arr[mid]:
        return BSearch(num, arr, low, mid-1)
    else:
        return BSearch(num, arr, mid+1, high)

def binary_search(num, arr):
    index = BSearch(num, arr, 0, len(arr)-1)
    if len(arr) == 0 or index == -1:
        print("Not Found")
    else:
        print(index)

binary_search(7, [2, 3, 4, 7, 8])
binary_search(3, [2, 3, 4, 7, 8])
binary_search(30, [2, 3, 4, 7, 8])
binary_search(30, [])