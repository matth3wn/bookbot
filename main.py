def count_words(contents):
    return len(contents.split())

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    letter_dict = {}
    for word in file_contents.split():
        for letter in word:
            lower = letter.lower()
            if lower in letter_dict:
                letter_dict[lower] += 1
            else:
                letter_dict[lower] = 1
    letter_list = list(letter_dict)
    letter_list.sort()
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for word in letter_list:
        if word.isalpha():
            print(f"The '{word}' character was found {letter_dict[word]} times")
    print("--- End Report ---")

