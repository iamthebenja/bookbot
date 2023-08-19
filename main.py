def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = word_count(text)
    letters_dict = letter_count(text)
    sorted_list = sort_letters_count(letters_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print()

    for item in sorted_list:
        if not item["letter"].isalpha():
            continue
        print(
            f"The '{item['letter']}' character was found {item['count']} times"
        )

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    return len(text.split())


def letter_count(text):
    letters = {}
    for letter in text.lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


def sort_key(x):
    return x["count"]


def sort_letters_count(letters_dict):
    sorted = []
    for letter in letters_dict:
        sorted.append({"letter": letter, "count": letters_dict[letter]})
    sorted.sort(reverse=True, key=sort_key)
    return sorted


main()
