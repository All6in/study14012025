
def main():
    book_path = f"/mnt/c/fprojects/boot.dev/github.com/All6in/study14012025/Books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_in_book = get_characters_in_book(text)
    
    print(f"{num_words} words found in the document")
    for character, count in characters_in_book.items():
        print(f"The '{character}' character was found {count} times")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_characters_in_book(text):
    text = text.lower()
    characters_in_book = {}
    for character in text:
        if character in characters_in_book:
            characters_in_book[character] += 1
        else:
            characters_in_book[character] = 1
          
    return characters_in_book



if __name__ == "__main__":
    main()






