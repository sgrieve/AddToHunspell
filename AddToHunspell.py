import core
import sys


def Run(WordFile, HunPath, DictName='en_US.dic'):
    WordList = core.LoadWordList(WordFile)
    core.MakeBackup(HunPath, DictName)
    core.AppendWordsToDict(WordList, HunPath, DictName)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        Run(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        Run(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        sys.exit('\n{} needs 3 arguments:\n\n'
                 '[1] The name of the file containing words to be added \n'
                 '[2] The Hunspell dictionary path\n'
                 '[3] An optional dictionary name, defaults to:'
                 ' en_US.dic\n'.format(sys.argv[0]))
