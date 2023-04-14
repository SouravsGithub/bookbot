def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letters_dict = count_letters(text)
    sorted_list = sorted_character_list(letters_dict)
    sorted_dict = dict_sort(sorted_list, letters_dict)
    show_report(book_path, num_words, sorted_dict)


def get_book_text(path):
    with open(path) as file:
        return file.read()


def count_words(text):
    words_array = text.split()
    return len(words_array)


def count_letters(text):
    text = text.lower()
    letters = {}
    for i in range(0, len(text)):
        if text[i] in letters:
            letters[text[i]] += 1
        else:
            if text[i].isalpha():
                letters[text[i]] = 1
    return letters


def sorted_character_list(dict):
    character_array = []
    for letter in dict:
        character_array.append(letter)
    character_array.sort()
    return character_array


def dict_sort(sorted_list, letters_dict):
    sorted_dict = {}
    for item in sorted_list:
        sorted_dict[item] = letters_dict[item]
    return sorted_dict


def show_report(path, num_words, letters):
    print(f"--- Begin report of {path}")
    print(f"{num_words} words found in the document")
    for letter in letters:
        print(f"The {letter} character was found {letters[letter]} times")
    print("--- End report ---")


main()