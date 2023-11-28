def count_words(book):
    words = book.split()
    return len(words)

def count_letters(book):
    letters = {}
    for letter in book:
        lowercase_letter = letter.lower()
        if lowercase_letter in letters:
            letters[lowercase_letter] += 1
        else:
            letters[lowercase_letter] = 1
    return letters

def letters_sorted(letters_dict):
    sorted_letters = []
    for letter in letters_dict:
        sorted_letters.append({"letter": letter, "count": letters_dict[letter]})

    sorted_letters.sort(reverse=True, key=sort_key)
    return sorted_letters

def sort_key(dict):
    return dict["count"]

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

book_file = "books/frankenstein.txt"
text = get_book_text(book_file)
num_words = count_words(text)
letters_dict = count_letters(text)
letters_sorted_list = letters_sorted(letters_dict)

print(f"book: {book_file}")
print(f"There are {num_words} words in this book.")

for word in letters_sorted_list:
    if not word["letter"].isalpha():
        continue
    print(f"The '{word['letter']}' letter was found {word['count']} times")

print("Done")
