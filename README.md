# Add To Hunspell

Simple script which will take a list of words in a text file and will append them to a user's Hunspell dictionary as a quick and dirty way of adding words to the Atom spellchecker.

## Warning!
This is probably a really bad idea and I provide no warranty that this will not all end in tears.

## Usage
Give the script a textfile with a list of words, separated by commas, spaces or newlines, along with the path to the Hunspell dictionary to be edited. The script will make a backup called `<dictionary filename>.BACKUP` and append the list of words to the dictionary.

The code does not deal with affixes as this is a simple script to add some geomorphology terms for my thesis, but this may be added in the future if I have time. The code does not test for duplicate words and is only designed to work on Ubuntu. It may work on other flavors of Linux but will probably cause natural disasters if used on Windows. 
