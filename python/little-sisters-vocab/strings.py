from typing import List


def add_prefix_un(word: str) -> str:
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return "un" + word


def make_word_groups(vocab_words: List[str]) -> str:
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a of
    strings with the prefix applied, separated by ' :: '.
    """
    _ = "".join([vocab_words[0] + i + " :: " for i in vocab_words[1:-1]])
    return vocab_words[0] + " :: " + _ + vocab_words[0] + vocab_words[-1]


def remove_suffix_ness(word: str) -> str:
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    if word[-5:] == "iness":
        return word[:-5] + "y"
    elif word[-4:] == "ness":
        return word[:-4]
    else:
        return word


def noun_to_verb(sentence: str, index: int) -> str:
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    # if a list of sentences of indexes
    # _words = [i.split(" ")[j] for i, j in zip(sentence, index)]
    return (sentence.split(" ")[index]).replace(".", "") + "en"

# don't need this, just run python -m pytest strings_test.py
#
# if __name__ == "__main__":
#     from strings_test import LittleSistersVocabTest

#     testclass = LittleSistersVocabTest()
#     testmethods = [getattr(testclass, i) for i in dir(testclass) if i.startswith("test_")]
#     [print(i()) for i in testmethods]
