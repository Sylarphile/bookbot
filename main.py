def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = wordcount(text)
    character_count = get_character_count(text)
    listed_dict = split_dict(character_count)
    listed_dict.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document\n")
    print(create_report(listed_dict))
    print("--- End report ---")    
 #   print(text)
 #   print(f"Wordcount: {num_words}")
 #   print(character_count)


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


def split_dict(dict):
    dict_list = []
    for chara in dict:
        chara_dict = {}
        chara_dict["character"] = chara
        chara_dict["count"] = dict[chara]
        dict_list.append(chara_dict)
    return dict_list


def sort_on(dict):
    return dict["count"]


def create_report(listed_dict):
    report = ""
    for i in listed_dict:
        if i["character"].isalpha() == True:
            report += f"The '{i["character"]}' character was found {i["count"]} times\n"
    return report

main()
