# import matplotlib.colors as colors
# from word2number import w2n

FILE_PATH = r".\files\text example.txt"

text_file = open(FILE_PATH, 'r')
text_content = text_file.read()

# 1 - amount of lines in the text
amount_of_lines = text_content.count('\n') + 1
text_content = text_content.replace('\n', '')

text_words = text_content.split(' ')
# 2 - amount of words in the text
amount_of_words = len(text_words)


# 3 - amount of unique words
def remove_multiple_words(words_list, word):
    while words_list.count(word) > 0:
        words_list.remove(word)


text_words_copy = text_content.lower().split(' ')
i = 0
for word in text_words_copy:
    if text_words_copy[i+1:].count(word) != 0:
        remove_multiple_words(text_words_copy, word)
    i += 1
amount_of_unique_words = len(text_words_copy)

# 4 - length of average sentence and the maximal length
text_sentences = text_content.split('. ')
average_sentence_len = amount_of_words/len(text_sentences)
maximal_sentence = max(text_sentences, key=lambda sentence: len(sentence.split(' ')))
maximal_sentence_len = len(maximal_sentence.split(' '))

# 5 - popular word and popular word with meaning
popular_word = max(text_words, key=lambda word: text_words.count(word) if word not in text_words_copy else 0)
# popular_word_with_meaning = - check how to do

# 6 - longest sequence of words without the letter 'k'
# text_content_split_by_k = text_content.split('k')  # see how the check both k and K without using lower()
# meaning_words = list(map(lambda seq: ' '.join(list(filter(lambda word: word in text_words, seq.split(' ')))), text_content_split_by_k))
# text_content_split_by_k = meaning_words
# longest_seq = max(text_content_split_by_k, key=lambda seq: len(seq.split(' ')))

# start_index = 0
# k_index = text_content.lower().find('k')
# space_index = 0
# len_of_text = len(text_content)
# list_seq_without_k = []
# while k_index < len_of_text:
#     space_index = text_content.rfind(' ', start_index, k_index - 1)  # find the space before the word with the k
#     list_seq_without_k.append(text_content[start_index: space_index])  # save the sequence in list
#     start_index = text_content[k_index + 1:].find(' ')  # save the index for searching from him in the next time
#     k_index = text_content[start_index + 1:].lower().find('k')  # searching the next appearance of k
# longest_seq = max(list_seq_without_k, key=lambda seq: len(seq.split(' ')))
# 7 - highest number in the text

# 8 - list of colors in the text and numbers of their appearances


# 9 - characters in the text
list_of_optional_words_with_capital = [
    'I',
    'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
]

# add option of countries and nations
# think of accurate setting of how to know who is character
# don't save the same character twice in the list
words_with_capital = filter(lambda word: word[0].isupper() and word.lower() not in text_words, text_words)
characters_in_text = list(filter(lambda word: word not in list_of_optional_words_with_capital, words_with_capital))
common_character = max(characters_in_text, key=lambda character: text_words.count(character))

print("Number of lines in the text:", amount_of_lines)
print("------------------------------------")
print("Number of words in the text:", amount_of_words)
print("------------------------------------")
print("Number of unique words in the text:", amount_of_unique_words)
print("------------------------------------")
print("The average of sentence length:", average_sentence_len)
print("The maximal length of sentence:", maximal_sentence_len)
print("------------------------------------")
print("Common word in the text:", popular_word)
print("------------------------------------")
# print("The longest sequence of words without the letter k is: ", longest_seq)
print("------------------------------------")
print("The highest number in the text: ")
print("------------------------------------")
print("The colors in the text: ")
print("------------------------------------")
print("Characters in the text: ", characters_in_text)
print("The common character is: ", common_character)

