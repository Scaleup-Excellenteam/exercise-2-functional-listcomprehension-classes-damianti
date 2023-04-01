def count_words(txt):
    """

    :param txt: (string) The input string to be processed.
    :return lengths: (dict) A dictionary mapping each word in the input string to its length.
    """
    clean_text = ''.join(c for c in txt if c.isalpha() or c.isspace())

    lengths = {word: len(word) for word in clean_text.split()}

    return lengths


if __name__ == "__main__":
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """

    print(count_words(text))
