import pandas as pd
import random

# make a learning system
# make 1-word writing question
# support term - translation swappign
# look for QA and make the program accessible for users
# go play minecraft

WORD_LIST_FILE_NAME = "מחשבת.xlsx"
DEFENITIONS_COLUMN = "sayer"
TRANSLATIONS_COLUMN = "content"

def getSingleWordSet(wordList, index):
    # return: tuple (term, definition)
    wordListKeys = list(wordList.keys())

    value = wordList[wordListKeys[index]]
    key = wordListKeys[list(wordList.values()).index(value)]

    word = invertHebrewWord((key, value), (True, True))
    return word


def invertHebrewWord(word, whatToInvert):
    # recive: tuple (key, hebrew value),
    # tuple of Invert (InvertKey, InvertValue)
    # return: same list, hebrew value(s) reversed
    newWord = list(word)
    newWord = [value[::-1] if whatToInvert[index] else value for index, value in enumerate(newWord)]
    #newWord[1] = newWord[1][::-1]
    return tuple(newWord)


def createAmericanQuestion(wordList, index):
    # recive: index of word
    # prints an american question
    correctWord = getSingleWordSet(wordList, index)

    try: # less efficient, could get inverted condition used in invertHebrew
        answers = [correctWord, *generateWordOptions(wordList, list(wordList.keys()).index(correctWord[0]),3)]
    except ValueError:
        answers = [correctWord, *generateWordOptions(wordList, list(wordList.keys()).index(correctWord[0][::-1]),3)]
    random.shuffle(answers)
    printAmericanQuestionText(correctWord, answers)
    if input(">>>") == str(answers.index(correctWord)+1):
        print("~ Gamin ~")
    else:
        print("OOOmg",(answers.index(correctWord)+1))
        input(">>>")
    

def generateWordOptions(wordList, indexToAvoid, numberOfWords):
    # recive: the correct word's index (to not create duplicates),
    # the number of random words to generate
    # return: list of the random words
    incorrectWords = []
    for i in range(numberOfWords):
        num = random.randint(0, len(wordList)-1)
        while num == indexToAvoid:
            num = random.randint(0, len(wordList)-1)
        
        newWord = getSingleWordSet(wordList, num)
        incorrectWords.append(newWord)
    return incorrectWords


def printAmericanQuestionText(correctAnswer, answers):
    translationAnswers = [x[1] for x in answers]
    data = [f"\n{correctAnswer[0]}?",
    f"\n1. {translationAnswers[0]}".ljust(20),f"2. {translationAnswers[1]}",
    f"\n3. {translationAnswers[2]}".ljust(20),f"4. {translationAnswers[3]}"]

    print(*data)

if __name__ == "__main__":
    data = pd.read_excel(WORD_LIST_FILE_NAME)

    wordList = dict(zip(data[DEFENITIONS_COLUMN], data[TRANSLATIONS_COLUMN]))
    while True:
        createAmericanQuestion(wordList, random.randint(0, len(wordList)-1))
