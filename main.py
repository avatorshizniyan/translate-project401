import os.path


class Translate:
    sentence_lists = []

    def __init__(self):
        if not os.path.exists("en-fa.txt"):
            print("File not found in your directory")
    def english_to_persian(self, english_sentence):
        sentence_words = []
        self.sentence_lists = english_sentence.strip().split('.')
        for sentence in self.sentence_lists:
            for word in sentence.split():
                sentence_words.append(word)

        with open("en-fa.txt", encoding="utf-8") as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]

        for word in sentence_words:
            for line in lines:
                if word in line:
                    print(''.join(line.split("-")[1:]),end='')

    def persian_to_english(self, persian_sentence):
        sentence_words = []
        self.sentence_lists = persian_sentence.strip().split('.')
        for sentence in self.sentence_lists:
            for word in sentence.split():
                sentence_words.append(word)

        with open("en-fa.txt", encoding="utf-8") as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]

        for word in sentence_words:
            for line in lines:
                if word in line:
                    print(''.join(line.split("-")[:1]), end='')

    def add_new_word(self, english_word, persian_word):
        f = open("en-fa.txt", "a", encoding="utf_8_sig")
        f.write(f"{english_word} - {persian_word}\n")
        f.close()


if __name__ == '__main__':

    translate = Translate()
    while (True):
        print("*** Select an Option From List ***")
        print(
            " (1) Add new word\n",
            "(2) English2Persian\n",
            "(3) Persian2English\n",
            "(4) Exit",
        )
        print("please select an option: ")
        selected_option = int(input(""))

        if selected_option == 1:
            english_word = str(input("Please enter english word: "))
            persian_word = str(input("Please enter persian word: "))
            translate.add_new_word(english_word, persian_word)
            print("*** Successfully inserted ***")

        elif selected_option == 2:
            english_sentence = str(input("Please enter your english sentence & split with . : "))
            translate.english_to_persian(english_sentence)
            # print("\n")

        elif selected_option == 3:
            english_sentence = str(input("Please enter your persian sentence & split with . : "))
            translate.persian_to_english(english_sentence)
            print("\n")

        elif selected_option == 4:
            print("You are out of the program")
            break
