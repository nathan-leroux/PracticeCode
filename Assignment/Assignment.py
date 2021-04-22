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
    return sentence.split()

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
    for word in stop_words:
        sentence = sentence.replace(f'\s{word}\s', '')

    return sentence


def remove_punc(sentence, punctuation):
    """
    Function takes a sentence and a string of punctuation and removes that punctuation from
    the sentence.
    """
    punctuation = tokenization(punctuation)
    for symbol in punctuation:
        sentence = sentence.replace(symbol,'')

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

    for word in sentence_copy:
        # removing words with undesirable characters/sequences
        print(word)
        for char in undesirable:
            print(f'testing char {char}')
            if char in word:
                print(f'removing word {word}')
                sentence.remove(word)
        # removing newline char from words
        if '\n' in word:
            re.sub('\n', '', word)
        #replacing '&and' with '&'
        if '&amp' in word:
            print('&amp found')
            word.replace('&amp', '&')

    #rejoining sentence
    result = ' '.join(sentence)
    return result


def construct_ngrams(sentence, n):
    """
    takes a sentence and a value for n. Then returns a list of ngrams with the length n, if no ngrams
    can be constructed, an empty list is returned.
    """
    sentence = tokenization(sentence)
    step = 0
    result = []
    while sentence[n + step] != sentence[-1]:
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
    index = 0
    for word in sentence:
        #removing ownerships
        if word.endswith('\'s') or word.endswith('s\''):
            sentence[index] = trim_word(word, ['\'s', 's\''])
        #removing plurals
        if (word.endswith('s')
            and not word.endswith()):
            print('yee')
        index += 1







if __name__ == '__main__':
    test_sentence = 'httpTHIS? is, A. #DuMb Sentence'
    stop_word_test = 'is and'
    punctuation_test = ', . ?'
    print(f'result: {cleaning_noise(test_sentence)}')

