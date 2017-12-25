# -*- coding: utf-8 -*-
def checkio(text):
    count = {}
    for character in text.lower():
    	if character.isalpha():
    		count.setdefault(character, 0)
    		count[character] = count[character] + 1
    count = sorted((key, value) for (key, value) in count.items())
    count = sorted(count, key=lambda x: -x[1])
    return (count[0][0])

def checkio_2(text):
    letters = [ch for ch in text.lower() if ch.isalpha()]
    letter_count = {ch: letters.count(ch) for ch in set(letters)}
    return max(sorted(letter_count), key=letter_count.get)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
