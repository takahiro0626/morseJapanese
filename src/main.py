class MorseJapanese:
    def __init__(self, words):
        self.codes = {
            "ア": "--･--"
        }
        self.words = words

    def translateJapaneseToMorse(self):
        letters = list(self.words)
        output = ""
        for letter in letters:
            if letter in self.codes:
                output += self.codes[letter] + " "
            else:
                return KeyError
        return output
