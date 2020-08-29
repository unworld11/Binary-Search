def bSearch(key,arr):
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    while low <= high:
        if key == arr[mid]:
            print(mid)
            return 0

        elif key < arr[mid]:
            high = mid - 1
        else :
            low = mid + 1
    else:
        print("Not Found")




