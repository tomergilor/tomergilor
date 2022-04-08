import os
#import FileData


class FileData():
    def __init__(self, file_name=None, word=None, counter=None):
        self.file_name = file_name
        self.word = word
        self.counter = counter


class WordCounter():
    def __init__(self):
        self.arr_files = []

    arr_file_data = []

    # The function searches, in a folder, files with extension and initializes and add them to arr_files array
    def searchFile(self, root_dir, ext_file):
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith(ext_file):
                    print (os.path.join(root, file))
                    self.arr_files.append(os.path.join(root, file))

    def find_words_in_files(self, arr_word_to_search, arr_word_to_exclude = None):
        if len(self.arr_files) != 0:
            for file in range(len(self.arr_files)):
                for word in range(len(arr_word_to_search)):
                    if arr_word_to_exclude == None or arr_word_to_search[word] not in arr_word_to_exclude:
                        self.read_word_in_file(arr_word_to_search[word], self.arr_files[file])
        else:
            print ("The arr_files is not initialized")

    def read_word_in_file(self, find_word, file):
        count = 0
        read_file = open (file , "r")
        for word in read_file.read().split():
            if word == find_word:
                count += 1

        self.arr_file_data.append(FileData(file, find_word, count))

        print ("In file " + file + " The word " + find_word + " Appears " + str(count) + " times")
