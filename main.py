def main():
    book_location = "books/frankenstein.txt"
    text = get_book_content(book_location)
    num_words = get_book_word_count(text)
    num_letters = get_book_letter_count(text)

    print(f"--- Begin report of {book_location} ---")
    print(f"There are {num_words} words found in the document. \n")
    for letter in num_letters:
        print(f"The '{letter[0]}' character was found {letter[1]} times.")

def get_book_content(path):
    with open(path) as f:
        return f.read()         

def get_book_word_count(text):
    words = text.split()
    return len(words)

def get_book_letter_count(text):
    words = text.lower()
    letter_count = {}
    for letter in words:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    letter_count_list = list(letter_count.items())
    letter_count_list.sort()
    return letter_count_list



main()