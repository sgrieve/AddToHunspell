import os
import sys


def IdentifySeparator(RawWords):
    """
    """
    if (',' in RawWords or ', ' in RawWords):
        return ','
    elif ' ' in RawWords:
        return ' '
    elif '\n' in RawWords:
        return '\n'
    else:
        print
        print 'Word list is not correctly formatted, separator not found.'
        print 'Use commas, spaces or new lines.'
        print
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
    """
    with open(filename, 'r') as f:
        RawWords = f.read()

    RawWords = RawWords.strip()
    separator = IdentifySeparator(RawWords)

    return CleanWords(RawWords.split(separator))


def CleanWords(WordList):
    """
    """
    return [word.strip() for word in WordList]


def AppendWordsToDict():
    """
    """
    pass


print LoadWordList('Geomorphology.txt')
print LoadWordList('Geomorphology2.txt')
print LoadWordList('Geomorphology3.txt')
