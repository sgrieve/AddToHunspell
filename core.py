import os
import sys


def IdentifySeparator(RawWords):
    """
    Pass in a string of RawWords to identify the separator. Will only find
    commas (with or without a trailing space), spaces, and newlines.

    Returns the separator as a string.
    """
    if (',' in RawWords or ', ' in RawWords):
        return ','
    elif ' ' in RawWords:
        return ' '
    elif '\n' in RawWords:
        return '\n'
    else:
        print '\nWord list is not correctly formatted, separator not found.'
        print 'Use commas, spaces or new lines.\n'
        sys.exit()


def LoadDict():
    """
    """
    pass


def MakeBackup():
    """
    Timestamp these backups
    """
    pass


def LoadWordList(filename):
    """
    Take a filename and load the words contained in that file, returning a list
    of words, cleaned to remove separators and whitespace.
    """
    try:
        with open(filename, 'r') as f:
            RawWords = f.read()

        RawWords = RawWords.strip()
        separator = IdentifySeparator(RawWords)

        return CleanWords(RawWords.split(separator))
    except:
        print '\nWord list file - {} - not found.\n'.format(filename)
        sys.exit()


def CleanWords(WordList):
    """
    Pass in a wordlist and this method will return the same list of words,
    with no whitespace either side of each word.
    """
    return [word.strip() for word in WordList]


def AppendWordsToDict():
    """
    """
    pass


print LoadWordList('Geomorphology.txt')
print LoadWordList('Geomorphology2.txt')
print LoadWordList('Geomorphology3.txt')
print LoadWordList('Geomorphology4.txt')
