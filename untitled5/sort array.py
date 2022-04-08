##################################
# Function that sorting an array:
##################################

arr = [2,4,3,5,1]
print arr       # Before sorting


# function that sort an array
def sort_array(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


sort_array(arr)
print arr       # After sorting
