from tabulate import tabulate
from googletrans import Translator


class Finnish_Translator(object):
    def __init__(self, word, language):
        self.word = word
        self.language = language
        self.cursor = Translator(service_urls=["translate.google.com"])

    def __repr__(self):
        translated = self.cursor.translate(self.word,
                                           dest=self.language).text

        data = [["Language:", "Word or Language:"],
                ["English:", self.word],
                ["Finnish:", str(translated)]]

        table = str(tabulate(data, headers="firstrow"))
        return table


if __name__ == "__main__":
    while True:
        translate = input(r"Enter word or sentence (Quit to stop): ")
        language = "fi"
        print(Finnish_Translator(translate, language))
        if translate.upper() == "QUIT":
            break