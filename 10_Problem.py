# Problem 10: Count Words in a Sentence
# Write a Python function that takes a sentence as input and returns a 
# dictionary where the keys are words and the values are the counts of how 
# often each word appears in the sentence.


##################### FIRST METHOD ##########################

# def word_counter (word: str, string: str) -> int:
#     count: int = 0
#     words_in_string: list[str] = string.split()
#     for i in range(len(words_in_string)):
#         if words_in_string[i] == word:
#             count += 1
#     return count


# def word_count (string: str) -> dict:
#     word_dic: dict = {}
#     words: list[str] = string.split()
#     for i in range(len(words)):
#         counter: int = 0
#         counter = word_counter(words[i], string)
#         word_dic.update({words[i] : counter})
#     return word_dic

##################### SECOND METHOD ##########################

def count_occurrence_of_words (string: str) -> dict:
    word_dic: dict = {}
    words: list[str] = string.split()
    for word in words:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return word_dic
            

string: str = "this is a test this is only a test"
word_dictionary: dict = count_occurrence_of_words(string)
print(word_dictionary) # Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}


  

