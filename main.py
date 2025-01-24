def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = wordcount(text)
    character_count = get_character_count(text)
    print(text)
    print(f"Wordcount: {num_words}")
    print(character_count)


def book_text(path):
    with open(path) as f:
        return f.read()
    

def wordcount(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    lowered_text = text.lower()
    characters = {}
    for character in lowered_text:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters


main()
