def group_by(func, iterable):
    """

    :param func:
    :param iterable:
    :return:
    """
    result = {}

    for item in iterable:
        key = func(item)
        result.setdefault(key, []).append(item)

    # If the key is not already in the dictionary, create an empty list as the value
    return result


# Example usage
if __name__ == "__main__":
    grouped_items = group_by(len, ["hi", "bye", "yo", "try"])
    print(grouped_items)  # Output: {2: ['hi', 'yo'], 3: ['bye', 'try']}
