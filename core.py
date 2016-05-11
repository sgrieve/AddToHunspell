import os


def IdentifySeparator(RawWords):
    """
    """
    return '\n'


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

    return RawWords.split(separator)


def AppendWordsToDict():
    """
    """
    pass

print LoadWordList('Geomorphology.txt')
