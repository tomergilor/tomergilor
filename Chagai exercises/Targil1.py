#  Get numbers from user and add write to a file
#  Read all numbers from file and add to array.
# sort the arr and then divide numbers to evens and ods sorted (object oriented)

from classes.sort_array_class import SortArray
from classes.handle_with_file import  HandleWithFiles

mySort = SortArray()
handleFile = HandleWithFiles()
numbers = []
file_name = 'numbers2.txt'


# local function to validate input correctness
def validate_input(num):
    try:
        num = int(num)
        if 0 < num <= 32000:
            return True
        else:
            return False
    except:
        return False


# Get data from user, build all input data as an array, validate its correctness and send to Sort class.
while (1):
    try:
        input_num = input("Enter a number in INT format between 1 - 32,000 please  (for exit insert -1): ")
        if input_num == '-1':
            break     # "-1" means that user finished entering numbers
        elif validate_input(input_num):
            input_num = int(input_num)
            handleFile.write_to_file(input_num, file_name)     # write numbers to a file
            #mySort.arr_all.append(input_num)
        else:
            print("Wrong input data. Please try again. \n")
    except:
        print("unexpected exception!!!")

# Read all numbers from file and add to arr_all array
numbers = handleFile.read_from_file(file_name)
for i in numbers:
    mySort.arr_all.append(int(i))


print("The original Array is: " + str(mySort.arr_all))
mySort.sort_array(mySort.arr_all)
mySort.divide_even_ods_arrays()
