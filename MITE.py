from collections import defaultdict
import argparse

parser = argparse.ArgumentParser(description='''
MITE
This tool finds mutually recursive acronyms, or recursonyms.
Uses the english dictionary in /usr/share/dict/words by default.
''')

parser.add_argument('length', default=4, type=int, nargs='?', help='The number of letters in the recursonym')
parser.add_argument('--dictionary-path', dest='dictionaryPath', default='/usr/share/dict/words')

opts = parser.parse_args()

# return a set of all words (excluding proper nouns, etc.)
def getWords(dictionaryPath):
    with open(dictionaryPath) as f:
        wordList = f.read().split()
    return { word for word in wordList if word.islower() }

ALL_WORDS = getWords(opts.dictionaryPath)

# Returns a string of sorted unique letters in the given word
def calcKey(word):
    return ''.join(sorted(set(word)))

# returns the number of unique starting letters among the words in the given list
def uniqueStart(stringList):
    return len({ x[0] for x in stringList })

def findRecursonyms(length, wordList):
    sizedWords = [x for x in wordList if len(x) == length]

    wordMap = defaultdict(list)
    for word in sizedWords:
        key = calcKey(word)
        if len(key) == length:
            wordMap[key].append(word)

    wordMap = { key : wordMap[key] for key in wordMap 
                    if uniqueStart(wordMap[key]) == length }
    return wordMap

def printRecursonyms(wordMap):
    for key in wordMap:
        for word in wordMap[key]:
            print(word.upper())
        print('\n')

printRecursonyms( findRecursonyms(opts.length, ALL_WORDS) )
