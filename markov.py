"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path = sys.argv[1]):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()

    return contents


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    text in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following text:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string = text_string.split()

    for i in range (len(text_string) - 2):
        temp_key = []

        # Append something to temp_key
        for num in range(n):
            try:
                word = text_string[i + num]
                temp_key.append(word)
            except IndexError:
                continue

    # n = 3 (0, 1, 2)
    # ['word0', 'word1', 'word2', 'word3', 'word4', 'word5']
        temp_key = tuple(temp_key)
        # Check if temp_key
        if temp_key not in chains:
            chains[temp_key] = [text_string[n]]
        elif temp_key in chains:
            chains[temp_key].append(text_string[n])

        # word1, word2, word3 = text_string[i], text_string[i + 1], text_string[i + 2]
        # temp_key = (word1, word2)

        # if temp_key not in chains:
        #     chains[temp_key] = [word3]
        # elif temp_key in chains:
        #     chains[temp_key].append(word3)

    return chains

# print(make_chains(open_and_read_file(), 5))

def make_text(chains, n):
    """Return text from chains."""

    text = []

    initial_key = choice(list(chains.keys()))
    for word in initial_key:
        text.append(word)

    next_word = choice(list(chains[initial_key]))
    text.append(next_word)

    current_key = text[-n:]
    current_key = tuple(current_key)

    while current_key in chains:

        next_word = choice(list(chains[current_key]))
        text.append(next_word)

        current_key = text[-n:]
        current_key = tuple(current_key)

    return ' '.join(text)

print(make_text(make_chains(open_and_read_file(), 5), 5))

# # Open the file and turn it into one long string
# input_text = open_and_read_file()

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
