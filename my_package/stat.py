
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

# 8 - list of colors in the text and numbers of their appearances


print("Number of lines in the text:", amount_of_lines)
print("------------------------------------")
print("Number of words in the text:", amount_of_words)
print("------------------------------------")
print("Number of unique words in the text:", amount_of_unique_words)
print("------------------------------------")
print("The average of sentence length:", average_sentence_len)
print("The maximal length of sentence:", maximal_sentence_len)
