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
    :param sentence:
    :return:
    """
    return sentence.lower()

def tokenization(sentence):
    """
    Function takes a sentence and returns a list of the words.
    :param sentence:
    :return:
    """
    return sentence.split()

def stop_word_removal(sentence, stop_words):
    """
    Function takes a sentence and a string of stop words, then removes those words from
    the sentence.
    :param sentence:
    :param stop_words:
    :return:
    """
    stop_words = tokenization(stop_words)
    for word in stop_words:
        sentence = sentence.replace(f'\s{word}\s', '')

    return sentence


def remove_punc(sentence, punctuation):
    """
    Function takes a sentence and a string of punctuation and removes that punctuation from
    the sentence.
    :param sentence:
    :param punctuation:
    :return:
    """
    punctuation = tokenization(punctuation)
    for symbol in punctuation:
        sentence = sentence.replace(symbol,'')

    return sentence


def remove_duplicate_words(sentence):
    """

    :param sentence:
    :return:
    """


test_sentence = 'THIS? is, A. DuMb Sentence'
stop_word_test = 'is and'
punctuation_test = ', . ?'
print(proper_capitalization(test_sentence))
print(tokenization(test_sentence))
print(stop_word_removal(test_sentence, stop_word_test))
print(remove_punc(test_sentence, punctuation_test))

