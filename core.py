import os
import sys
import shutil
import time


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


def MakeBackup(HunPath, DictName='en_US.dic'):
    """
    Create a timestamped backup of the Hunspell dictionary in the same location.
    """
    if os.path.exists(HunPath + DictName):
        TimeStamp = time.strftime('%d-%m-%Y_%H%M', time.localtime())
        BackupName = ('.BACKUP_' + TimeStamp)
        shutil.copy(HunPath + DictName, HunPath + DictName + BackupName)
    else:
        print '\nHunspell dictionary - {}{} - not found.\n'.format(HunPath,
                                                                   DictName)
        sys.exit()


def LoadWordList(Filename):
    """
    Take a filename and load the words contained in that file, returning a list
    of words, cleaned to remove separators and whitespace.
    """
    try:
        with open(Filename, 'r') as f:
            RawWords = f.read()

        RawWords = RawWords.strip()
        separator = IdentifySeparator(RawWords)

        return CleanWords(RawWords.split(separator))
    except:
        print '\nWord list file - {} - not found.\n'.format(Filename)
        sys.exit()


def CleanWords(WordList):
    """
    Pass in a wordlist and this method will return the same list of words,
    with no whitespace either side of each word.
    """
    return [word.strip() for word in WordList]


def AppendWordsToDict(WordList, HunPath, DictName='en_US.dic'):
    """
    Load the Hunspell dictionary and append the supplied words to it.
    """
    try:
        with open(HunPath + DictName, 'a') as f:
            for word in WordList:
                f.write(word + '\n')

        print '\nSUCCESS - {} words written '\
            'to the dictionary.\n'.format(len(WordList))

    except:
        print '\nHunspell dictionary - {}{} - not found.\n'.format(HunPath,
                                                                   DictName)
        sys.exit()


words = LoadWordList('Geomorphology.txt')
MakeBackup('/home/sgrieve/test/', 'test.txt')
AppendWordsToDict(words, '/home/sgrieve/test/', 'test.txt')
