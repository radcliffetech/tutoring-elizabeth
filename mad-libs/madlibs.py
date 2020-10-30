from gtts import gTTS
import re
import subprocess


def fill_out_words(text):
    """This function populates the madlibs

    Just remember that the prompts have to have no spaces, so:
    * [PLURAL_NOUN] instead of [PLURAL NOUN]

    """
    inputs = re.findall("\[(\_|\w+)\]", text)  # noqa

    # collect answers and update the story
    for name in inputs:
        response = input(f'enter a {name}: ')
        # text.replace(from, to, number of times to do the change)
        text = text.replace(f"[{name}]", response, 1)

    # the text is finished!
    return text


text = """
A letter to my [NOUN]

Dear [NAME],

Computer Science is so [ADJECTIVE]! The [PLURAL_NOUN] are very [ADJECTIVE],
especially when they are [VERB].

Today we are [ADVERB] learning about [PLURAL_NOUN]. The teacher, [NAME], is very [ADJECTIVE].
They are always saying "[PHRASE]".

We took a test about [NOUN], and I got a [NUMBER] out of [NUMBER].

You should take this class, it is [ADJECTIVE] like a [NOUN].

[FAREWELL_WORD],
[NAME]
"""

finished_text = fill_out_words(text)

print(finished_text)

name = input('What is your name: ')

filename = f"{name.lower()}_hilarious.mp3"

# this runs the text to speech and saves it to a file
myobj = gTTS(text=finished_text, lang='en', slow=False)
myobj.save(filename)

# this plays the mp3 file
subprocess.call(f"afplay {filename}", shell=True)
