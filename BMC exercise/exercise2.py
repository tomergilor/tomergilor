import os
import WordCount2

arr_word_to_search = ["Error", "Fatal", "Fail"]
arr_word_to_exclude = ["Error"]
ext_file = '.log'
root_dir = 'C:\\logs'

word_count = WordCount2.WordCounter()


word_count.searchFile(root_dir, ext_file)
word_count.find_words_in_files(arr_word_to_search)

