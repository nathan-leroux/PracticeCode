"""
Nathan Le Roux
24476883
CITS2401 Assignment 2
Tweet Analysis in Python
"""
import re


def proper_capitalization(sentence):
    """
    Function takes a sentence and returns it with all letters in lower case.
    """
    return sentence.lower()


def tokenization(sentence):
    """
    Function takes a sentence and returns a list of the words.
    """
    result = sentence.split()
    return result


def trim_word(word, bin_list):
    """
    Takes a word and a list of chars to remove from end of word, returns trimmed word
    (not required for assignment, writing this to make my life easier)
    """
    result = word
    for item in bin_list:
        if word.endswith(item):
            result = word[0:-len(item)]
    return result


def stop_word_removal(sentence, stop_words):
    """
    Function takes a sentence and a string of stop words, then removes those words from
    the sentence.
    """
    stop_words = tokenization(stop_words)
    list_of_words = tokenization(sentence)
    for word in stop_words:
        breaker = False
        while breaker is False:
            breaker = True
            if word in list_of_words:
                list_of_words.remove(word)
                breaker = False

    result = ' '.join(list_of_words)
    return result

def remove_punc(sentence, punctuation):
    """
    Function takes a sentence and a string of punctuation and removes that punctuation from
    the sentence.
    """
    sentence = tokenization(sentence)
    for char in punctuation:
        flag = False
        while flag is False:
            flag = True
            for word in sentence:
                if word.endswith(char):
                    index = sentence.index(word)
                    sentence[index] = word[0:-1]
    ' '.join(sentence)

    return sentence


def remove_duplicate_words(sentence):
    """
    Takes a sentence, removes any duplicate words, returns a string with words in alphabetical order
    """
    #removing duplicate words
    unique_words = []
    sentence = tokenization(sentence)
    for word in sentence:
        if word not in unique_words:
            unique_words.append(word)

    #putting in alphabetical order and rejoining
    unique_words.sort()
    result = ' '.join(unique_words)
    return result


def cleaning_noise(sentence):
    """
    Takes a Sentence and removes all words not useful for text analysis
    """
    sentence = tokenization(sentence)
    sentence_copy = sentence.copy()
    undesirable = ['http', '@', '#']
    count = 0
    # removing words with undesirable characters/sequences
    for char in undesirable:
        for word in sentence_copy:
            if char in word:
                if char == '@':
                    count +=1
                    if count % 2 == 1:
                        sentence.remove(word)
                else:
                    sentence.remove(word)

    sentence = ' '.join(sentence)
     # removing newline char from words
    if '\n' in sentence:
        sentence = sentence.replace('\n', '')
    #replacing '&and' with '&'
    if '&amp' in sentence:
        sentence = sentence.replace('&amp', '&')

    #rejoining sentence

    return sentence


def construct_ngrams(sentence, n):
    """
    takes a sentence and a value for n. Then returns a list of ngrams with the length n, if no ngrams
    can be constructed, an empty list is returned.
    """
    sentence = tokenization(sentence)
    step = 0
    result = []
    while n + step <= len(sentence):
        ngram = []
        for x in range(n):
            ngram.append(sentence[x+step])
        result.append(ngram)
        step += 1

    return result

def pos(sentence):
    """
    Takes a sentence and stems words to thier basic forms, returns a string of stemmed words
    """
    sentence = tokenization(sentence)
    count = 0
    while count != 2:
        count += 1
        for word in sentence:
            index = sentence.index(word)
            #removing ownerships
            if re.search("\'s$|s\'$", word):
                sentence[index] = re.sub("\'s$|s\'$", '', word)
            #removing plurals
            elif re.search("sses$", word):
                sentence[index] = re.sub("sses$", 'ss', word)
            elif len(word) > 4 and re.search("ies$", word):
                sentence[index] = re.sub("ies$", 'i', word)
            elif re.search("[aeiouyAEIOUY]", word) and re.search("s$", word) and not re.search("[aeiousy]s$", word):
                sentence[index] = re.sub("s$", '', word)
            #removing adjectives
            elif re.search("er$", word):
                sentence[index] = re.sub("er$", '', word)
            #removing past tense
            elif len(word) <= 4 and re.search("ied$", word):
                sentence[index] = re.sub("ied$", 'ie', word)
            elif re.search("ed$", word):
                sentence[index] = re.sub("ed$", '', word)
            #removing verbs
            elif len(word) > 5 and re.search("ing$", word):
                sentence[index] = re.sub("ing$", '', word)
            #removing adverbs
            elif re.search("ly$", word):
                sentence[index] = re.sub("ly$", '', word)

    result = ' '.join(sentence)
    return result


def load_data(filename):
    """
    Takes a filename (string) and returns a list containing all the lines of text
    """
    file = open(filename, mode='r', encoding='utf8')
    return file.readlines()


def tweet_analysis():
    """
    Takes user inputs and calls previous functions to complete tweet analysis.
    Writes the results to file and returns them.
    """
    #Ask for user input
    input_file_name = input('Enter the name of the file to read: ')
    output_file_name = input('Enter the name of the file to write: ')
    stopwords = input('Enter your stopwords: ')
    punctuations = input('Enter your punctuations to remove: ')

    #Call previous functions
    file_lines = load_data(input_file_name)
    output_lines = []
    output_file = open(output_file_name, mode='w', encoding='utf8')

    for sentence in file_lines:
        sentence = proper_capitalization(sentence)
        sentence = stop_word_removal(sentence, stopwords)
        sentence = remove_punc(sentence, punctuations)
        sentence = remove_duplicate_words(sentence)
        sentence = cleaning_noise(sentence)
        sentence = pos(sentence)

        output_lines.append(sentence)
        output_file.write(f'{sentence}\n')

    return output_lines


def word_ranking(corpus, n):
    """
    Takes a list of sentences and counts the frequency of each word.
    Returns the top n most frequent words in tuples
    """
    #counting words
    unique_words = {}
    for sentence in corpus:
        word_list = tokenization(sentence)
        for word in word_list:
            if word in unique_words:
                unique_words[word] += 1
            elif word != '':
                unique_words.setdefault(word, 1)
    #showing top n words
    result = []

    while len(result) != n:
        max_value = 0
        for value in unique_words.values():
            if value > max_value:
                max_value = value
        for key, value in unique_words.items():
            if value == max_value and max_value > 0:
                result.append((key, value))
                unique_words[key] = 0
    result.sort()
    return result


