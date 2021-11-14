from colour import Color
from word2number import w2n


FILE_PATH = r".\files\text example.txt"
# FILE_PATH = r".\files\dickens.txt"


def remove_multiple_words(words_list, word):
    while words_list.count(word) > 0:
        words_list.remove(word)


text_file = open(FILE_PATH, 'r', errors='ignore')
text_content = text_file.read()

# 1 - amount of lines in the text
amount_of_lines = text_content.count('\n') + 1
text_content = text_content.replace('\n', ' ')

text_words = text_content.split(' ')
remove_multiple_words(text_words, '')
text_words = list(map(lambda word: word.replace('.', '').replace(',', '').replace(';', ''), text_words))

# 2 - amount of words in the text
amount_of_words = len(text_words)

# 3 - amount of unique words
text_words_copy = text_content.lower().split(' ')
i = 0
for word in text_words_copy:
    if text_words_copy[i + 1:].count(word) != 0:
        remove_multiple_words(text_words_copy, word)
    i += 1
amount_of_unique_words = len(text_words_copy)

# 4 - length of average sentence and the maximal length
text_sentences = text_content.split('. ')
average_sentence_len = round(amount_of_words / len(text_sentences), 2)
maximal_sentence = max(text_sentences, key=lambda sentence: len(sentence.split(' ')))
maximal_sentence_len = len(maximal_sentence.split(' '))

# 5 - popular word and popular word with meaning
popular_word = max(text_words, key=lambda word: text_words.count(word) if word not in text_words_copy else 0)
list_syntax_words = ['am', 'is', 'are', 'do', 'does',
                     "isn't", "aren't", "don't", "doesn't",
                     'was', 'were',
                     "wasn't", "weren't",
                     'had', 'have', 'has',
                     'that', 'the',
                     'will', "won't",
                     'be', 'been',
                     'a', 'an',
                     'of', 'and', 'because', 'so', 'as', 'but', 'for', 'such', 'to', 'in'
                     ]
popular_word_without_syntax = max(text_words,
                                  key=lambda word: text_content.lower().count(word.lower()) if word.lower() not in list_syntax_words else 0)

# 6 - longest sequence of words without the letter 'k'
start_index = 0
k_index = text_content.lower().find('k')
space_index = 0
len_of_text = len(text_content)
list_seq_without_k = []
while k_index != -1:
    space_index = text_content.rfind(' ', start_index, k_index - 1)  # find the space before the word with the k
    list_seq_without_k.append(text_content[start_index: space_index])  # save the sequence in list
    start_index = text_content.find(' ', k_index + 1) + 1  # save the index for searching from him in the next time
    k_index = text_content.lower().find('k', start_index, len_of_text)  # searching the next appearance of k
longest_seq = max(list_seq_without_k, key=lambda seq: len(seq.split(' ')))

# 7 - highest number in the text
list_numbers = []
number_sentence = ""
for word in text_words:
    if word.isdigit():
        list_numbers.append(int(word))
    else:
        try:
            word_as_number = w2n.word_to_num(word)
            number_sentence += word + ' '
        except ValueError:
            if number_sentence != "" and word != "and":
                list_numbers.append(w2n.word_to_num(number_sentence))
                number_sentence = ""
highest_number = max(list_numbers)


# 8 - list of colors in the text and numbers of their appearances
def check_color(color):
    try:
        Color(color)
        return True
    except ValueError:
        return False


color_dic = dict()
for word in text_words:
    if check_color(word):
        color_dic[word] = text_words.count(word)


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
print("Common word (not syntax word):", popular_word_without_syntax)
print("------------------------------------")
print("The longest sequence of words without the letter k is: ", longest_seq)
print("------------------------------------")
print("The highest number in the text: ", highest_number)
print("------------------------------------")
print("The colors in the text: ", color_dic)



