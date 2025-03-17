from stats import count_words_in_book, count_char_from_string
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(count_words_in_book(text))
        print("--------- Character Count -------")
        char_count = count_char_from_string(text)
        for char_obj in char_count:
            if char_obj["char"].isalpha():
                print(char_obj["char"] + ": " + str(char_obj["count"]))
                
        print("============= END ===============")

def get_book_text(path: str):
    with open(path) as f:
        file_content = f.read()
        return file_content

main()