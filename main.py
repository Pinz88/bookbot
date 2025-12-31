import sys
from stats import count_words,count_characters, sort_characters_by_count, print_character_count_list

def get_book_text(path_to_file):
    file_contents = None
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    word_count = count_words(book_text)
    character_dic = count_characters(book_text)
    sorted_character_list = sort_characters_by_count(character_dic)
    print_character_count_list(sorted_character_list,path_to_file, word_count)

main()