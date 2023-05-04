with open('books/frankenstein.txt') as f:
    file_content = f.read()
    words = file_content.split()
    letters = {}
    list_letters = []

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")

    for word in words:
        for letter in word:
            lower_letter = letter.lower()
            if lower_letter in letters:
                letters[lower_letter] += 1
            else:
                letters[lower_letter] = 1

    for letter in letters:
        if letter.isalpha():
            list_letters.append({"letter": letter, "count": letters[letter]})
    
    list_letters.sort(reverse=True, key=lambda x: x["count"])
    
    for item in list_letters:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    print("--- End report ---")
              