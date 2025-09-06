from stats import word_count, character_count, character_report
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        fileContents = f.read()
        return fileContents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    BOOKPATH = sys.argv[1]
    #BOOKPATH = "./books/test.txt" # test
    print("============== BOOKBOT ==========")
    print(f"Analyzing book found at {BOOKPATH}")
    bookText = get_book_text(BOOKPATH)
    print("------------- Word Count --------")
    print("found ", word_count(bookText), " total words")
    print("----------- Character Count -----")
    charDict = character_count(bookText)
    reportList = character_report(charDict)
    for i in reportList:
        char = i["char"]
        num = i["num"]
        print(f"{char}: {num}")
    print("================ END ============")


main()
