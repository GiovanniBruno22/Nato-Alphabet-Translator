
def populate_dictionary():
    """Populates the nato alphabet translator from the alphabet.txt.
    
       Returns: temp_dict (dict), the dictionary with all the letters and their NATO equivalent.
    """
    temp_dict = {}
    with open ("src/alphabet.txt", "r") as alphabet:
        words = [word.strip("\n") for word in alphabet]
        for word in words:
            temp_dict[word[0]] = word
    return temp_dict


def main():
    """Core functionality of the script."""
    nato_alphabet_translator = populate_dictionary()
    word = input("Welcome to Nato Alphabet Translator, please type in a word to be translated:\n").strip(" ").upper()
    for letter in word:
        if letter not in nato_alphabet_translator:
            print("Invalid word, please try again.")
            exit()
    print("Here's your translated word: \n")
    for letter in word:
        print(nato_alphabet_translator[letter])


if __name__ == "__main__":
    main()