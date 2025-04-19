def word_counter(book_contents):
    words = book_contents.split()
    return (len(words))

def char_counter(book_contents):
    character_count = {}
    for character in book_contents:
        character = character.lower()
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count


def sort_char_count(character_count):
    char_list = []
    for char, count in character_count.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]  
    
    char_list.sort(reverse = True, key = sort_on)

    return char_list
    
    











def sorter(character_count, filepath, num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = sort_char_count(character_count)
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
        else:
            pass
    
    
    print("============= END ===============")


