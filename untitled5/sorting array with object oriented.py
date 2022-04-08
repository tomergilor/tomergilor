#  Get numbers from user and add numbers to array.
#  All even numbers add to even arr and all ods number to ods arr.
#  Sort the 2 arrs ASC.


class Arrays(object):
    def __init__(self):
        self.arr_all = []
        self.arr_even = []
        self.arr_ods = []

    def validate_input(self, num):
        while True:
            try:
                x = int(num)
                if x < -1 and x > 32000:
                    break
                else:
                    return num

            except ValueError:
                print "Oops!  That was no valid number.  Try again..."

    # Function that sorting array
    def sort_array(self, arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    # divide even and ods numbers to 2 arrays
    def divide_even_ods_arrays(self, arr):
        for i in self.arr_all:
            if i % 2 == 0:
                self.arr_even.append(i)
            else:
                self.arr_ods.append(i)
        print "The even array is : " + str(self.arr_even)
        print "The ods array is : " + str(self.arr_ods)

        # sort the even array
        print "The even array after sorting : " + str(self.sort_array(self.arr_even))

        # sort the ods array
        print "The even array after sorting : " + str(self.sort_array(self.arr_ods))

    # get numbers from user and add to global array:
    def add_global_arr(self):
        user_num = int(input("Enter your number (for exit insert -1) :"))
        #self.validate_input(user_num)
        while (user_num != -1):
                val = int(user_num)
                self.arr_all.append(val)
                user_num = int(input("Enter your number (for exit insert -1) :"))
        print "The global array is: " + str(self.arr_all)
        self.sort_array(self.arr_all)
        self.divide_even_ods_arrays(self.arr_all)


ar = Arrays()
ar.add_global_arr()

