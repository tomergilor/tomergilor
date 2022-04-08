

class SortArray(object):
    def __init__(self):
        self.arr_all = []
        self.arr_even = []
        self.arr_ods = []
        self.arrNumbers = []

    # Function that sorting array
    def sort_array(self, arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    # divide even and ods numbers to 2 arrays
    def divide_even_ods_arrays(self):
        for i in self.arr_all:
            if i % 2 == 0:
                self.arr_even.append(i)
            else:
                self.arr_ods.append(i)
        # print "The even array is : " + str(self.arr_even)
        # print "The ods array is : " + str(self.arr_ods)

        # sort the even array
        print("The even array after sorting : " + str(self.sort_array(self.arr_even)))

        # sort the ods array
        print("The ods array after sorting : " + str(self.sort_array(self.arr_ods)))


