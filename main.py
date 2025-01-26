def main ():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    count = word_count(text)
    characters = char_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document\n")

    for char_dict in characters:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- end report ---")    


#def sort(characters):



def char_count(text):
    characters = {}
    for char in text.lower():
        if char.isalpha():
            characters[char] = characters.get(char, 0) + 1

    list_of_characters = [{'char': key, 'num': value} for key, value in characters.items()]
    sorted_list = sorted(list_of_characters, key=lambda x: x['num'], reverse=True)
    return sorted_list


def word_count(text):
    words = text.split()
    return len(words)


def book_text(path):
    with open(path) as f:
        return f.read()


main()
