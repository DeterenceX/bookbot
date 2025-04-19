import sys
from stats import word_counter
from stats import char_counter
from stats import sorter


    
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

        

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():
    book_contents = get_book_text(filepath)
    num_words = word_counter(book_contents)
    num_chars = char_counter(book_contents)
    sorter(num_chars, filepath, num_words)

    
 

main()
 