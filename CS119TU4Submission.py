
def main (wordList):
    wordCount = 0 
    enterWord = input("please enter at least 8 words (type STOP to end list): ")
    while True: 
        
        if enterWord != 'STOP':
            wordList.append(enterWord)
            wordCount = wordCount + 1
            enterWord = input("please enter at least 8 words (type STOP to end list): ")
        elif enterWord == 'STOP' and wordCount<=7:
            print("Sorry, but you need at least 8 words")
            enterWord = input("please enter at least 8 words (type STOP to end list): ")
            wordList.append(enterWord)
            wordCount = wordCount + 1
        else:
            break
    print("Entered list is: \n",wordList)
            
    



def SortByIncreasingLength(wordList):
    wordList1 = wordList[:]
    wordList1.sort(key=len)
    print("Words sorted from smallest to biggest: \n",wordList1)


def SortByDecreasingLength(wordList):
    wordList2 = wordList[:]
    wordList2.sort(key=len, reverse=True)
    print("Words sorted from biggest to smallest: \n",wordList2)

def SortByTheMostVowels(wordList):
    wordList3 = wordList[:]
    def sortalg(wordList3):
        wordCount = 0
        for z in wordList3:
            if z in ['a', 'e', 'i', 'o','u','A','E','I','O','U']:
                wordCount = wordCount + 1
        return wordCount
    wordList3.sort(key=sortalg)
    print("Words sorted from least to most vowels: \n",wordList3)

def SortByTheLeastVowels(wordList):
    wordList4 = wordList[:]
    def sortalg2(wordList4):
        wordCount = 0
        for z in wordList4:
            if z in ['a', 'e', 'i', 'o','u','A','E','I','O','U']:
                wordCount = wordCount + 1
        return wordCount
    wordList4.sort(key=sortalg2, reverse = True)
    print("Words sorted from most to least vowels: \n",wordList4)

def CapitalizeEveryOtherCharacter(wordList):
    wordList5 = wordList[:]
    charIsLower = True
    newList = []
       
    for z in wordList5:
        for k in z:
            if not k.isalpha():
                newList.append(k)
                continue
            if charIsLower:
                newList.append(k.upper())
            else:
                newList.append(k.lower())
            charIsLower = not charIsLower
            wordList5 = newList
    print("Every other letter capitalized: \n",wordList5)

def ReverseWordOrdering(wordList):
    wordList6 = wordList[:]
    wordList6 = wordList6[::-1]
    print("Words sorted in reverse: \n",wordList6)

def FoldWordsOnMiddleOfList(wordList):
    wordList7 = wordList[:]
    middle = (len(wordList7) - 1)//2

    print("Word in middle of list: \n", wordList7[middle])

wordList = []
main(wordList)
SortByIncreasingLength(wordList)
SortByDecreasingLength(wordList)
SortByTheMostVowels(wordList)
SortByTheLeastVowels(wordList)
CapitalizeEveryOtherCharacter(wordList)
ReverseWordOrdering(wordList)
FoldWordsOnMiddleOfList(wordList)