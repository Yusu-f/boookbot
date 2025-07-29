from sys import argv, exit
from stats import count_characters, count_words, sort_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        
    text = get_book_text(argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    sort_characters(count_characters(text))
    print("============= END ===============")
    
if __name__ == "__main__":
    main()