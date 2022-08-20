"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path = sys.argv[1]):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    # print(contents)

    return contents

# open_and_read_file()

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string = text_string.split()

    for i in range (len(text_string) - 1):
        try:
            word1, word2, word3 = text_string[i], text_string[i + 1], text_string[i + 2]
            temp_key = (word1, word2)

            if temp_key not in chains:
                chains[temp_key] = [word3]
            elif temp_key in chains:
                chains[temp_key] += [word3]
        except IndexError:
            continue
    #print(chains)

    return chains

make_chains(open_and_read_file())

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    #while True:
    random_key = choice(list(chains.keys()))
    word1, word2 = random_key
    words.append(word1)
    words.append(word2)
    next_word = choice(list(chains[random_key]))
    words.append(next_word)
    new_tuple = (words[1], words[2])

    for key in chains:
        if key == new_tuple:
            next_word = choice(list(chains[new_tuple]))
            words.append(next_word)


    print(words)


  #  return ' '.join(words)

make_text(make_chains(open_and_read_file()))

# input_path = 'green-eggs.txt'

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
