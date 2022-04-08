

class HandleWithFiles(object):
    #def __init__(self):

    ## Function that write to a file
    def write_to_file(self, num, file_name):
        my_file = open(file_name, "a")
        my_file.write(str(num))
        my_file.close()

    def read_from_file(self, file_name):
        my_file = open(file_name, "r")
        with open(file_name) as text:
            #return [int(x) for x in text]
            for x in text:
                return x
