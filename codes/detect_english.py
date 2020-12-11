# is this sentence in english?

def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords


def strip_punctuation(message):
    UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def detect_english(message):

    acceptable_percentage = 0.5

    dictionary = loadDictionary()

    # strip punctuation!
    message = strip_punctuation(message)
    message = message.upper()

    english_words = 0
    words = message.split()

    for word in words:

        if word in dictionary:
            english_words += 1

    percentage_of_words = english_words / len(words)

    if percentage_of_words >= acceptable_percentage:
        return True
    else:
        return False


if __name__ == "__main__":
    phrases = [
        'tenaz5x3vNsv330QN1z5x3vNsv330Qaz5x3vNr33N yvN.rBQfyQN.yr Nw!5Nz Nz0N 6N9zuvQZ5NrN65vNy690vN67v5N03vzxy',
        'unicorn robot flserioasdf iuahsdfhkjlahdsf aer uiyoayseoiur aer hi there',
        "this is totally english",
        "four secore and a million years ago",
        "Hello, Elizabeth! this is a thing!!!"
    ]

    for phrase in phrases:
        print(phrase)
        is_english = detect_english(phrase)
        print(is_english)
