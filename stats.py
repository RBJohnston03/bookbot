# function that takes the text of a book and returns 
# the number of words in that book
def word_count(bookText):
    textList = bookText.split()
    return len(textList)


# function that takes the text of a book and returns a dictionary
# of string->int of the count of each character
def character_count(bookText):
    # initialize dictionary
    charCountDict = dict()

    # loop through each character in text and increment 
    # that char count in charCountDict
    for char in bookText:
        if char.lower() in charCountDict:
            charCountDict[char.lower()] = charCountDict[char.lower()] + 1
            #print(f"adding {char} to charCountDict as {char.lower()}, and the count is {charCountDict[char.lower()]}") #debug printout
        else:
            charCountDict[char.lower()] = 1
            #print(f"adding {char} to charCountDict as {char.lower()} for first time, count is {charCountDict[char.lower()]}") #debug printout
    
    return charCountDict


def sort_on(items):
    return items["num"]

# function that takes a character_count(bookText) formatted dictionary and
# returns a list of dictionaries where each dictionary contains a key-value
# pair for the character and the count. The list is returned sorted from
# greatest to least, and non alphabetical characters are dropped
def character_report(charCountDict):
    reportList = []
    for char in charCountDict:
        if char.isalpha():
            charDict = {"char":char, "num":charCountDict[char]}
            reportList.append(charDict)
    
    reportList.sort(reverse=True, key=sort_on)
    return reportList
