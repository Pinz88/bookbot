def sort_on(items):
    return items["num"]

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    character_set = {}
    words = book_text.split()
    
    for word in words:
        for char in word:
            lower_char = char.lower()
            if lower_char in character_set:
                character_set[lower_char] += 1
            else:
                character_set[lower_char] = 1
                
    return character_set

def sort_characters_by_count(character_dic):
    result = []
    for key in character_dic:
        new_dic = {}
        new_dic["char"] = key
        new_dic["num"] = character_dic[key]
        result.append(new_dic)
    result.sort(reverse=True, key=sort_on)
    return result

def print_character_count_list(character_list,path_to_file, word_count):
    print(f"Analyzing book found at {path_to_file}...")
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dic in character_list:
       if char_dic["char"].isalpha():
          print(f"{char_dic['char']}: {char_dic['num']}")
    print("============= END ===============")
    