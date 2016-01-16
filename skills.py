"""Skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    # make an empty set
    no_duplicates = set()

    # for each word in our input list, add it to our set
    # duplicates are automatically screened out, bc yay sets
    for word in words:
        no_duplicates.add(word)


    # return our output in the form of a list
    no_duplicates = list(no_duplicates)

    return no_duplicates


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([4, 3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    """

    #convert both input lists into sets to screen for unique words
    set1 = set(list1)
    set2 = set(list2)

    # use fancy set math to get the intersection, then convert into a list
    output = set1 & set2
    output = list(output)

    return output


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    # make an empty dictionary
    unique_dict = {}

    # take our input string and turn it into a list
    input_list = input_string.split(" ")

    # check each word to see if it's in our dictionary
    # the value of the wordth index is the number of times we've seen it
    # add it to the dictionary w/ a value of 1 if it's a new word
    # update value by adding 1 if we see it again
    for word in input_list:
        if word in unique_dict.keys():
            unique_dict[word] += 1
        else:
            unique_dict[word] = 1

    return unique_dict


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    # input phrase is a string
    # convert to list for ease of use
    # strings are iterable too, but over characters
    # i want to look at separate words
    list_phrase = phrase.split(" ")

    # make our pirate dictionary; keys are normal English
    # values are our pirate speak
    pirate_dict = {
                "sir": "matey",
                "hotel": "fleabag inn",
                "student": "swabbie",
                "boy": "matey",
                "madam": "proud beauty",
                "professor": "foul blaggart",
                "restaurant": "galley",
                "your": "yer",
                "excuse": "arr",
                "students": "swabbies",
                "are": "be",
                "lawyer": "foul blaggart",
                "the": "th'",
                "restroom": "head",
                "my": "me",
                "hello": "avast",
                "is": "be",
                "man": "matey",
                }

    # initialize empty output list, then convert to string later
    output_list = []
    for word in list_phrase:
        if word in pirate_dict.keys():
            output_word = pirate_dict[word]
        else:
            output_word = word
        output_list.append(output_word)


    # convert back into string for pretty output
    output_string = " ".join(output_list)

    return output_string


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items---the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    
    # make an empty dictionary, because yay dictionaries
    word_len_dict = {}

    # iterate over the words in our input list
    for word in words:
        len_word = len(word)

        # the lengths of our words are the keys of the dictionary
        # if we've seen that length before, add the word to the list of values
        # if we haven't seen it before, make that length a new key, and assign
        # it with a value of a list including the word
        if len_word in word_len_dict:
            word_len_dict[len_word].append(word)
        else:
            word_len_dict[len_word] = [word]


    # return a list of tuples with key: value pairs
    return word_len_dict.items()


def get_sum_zero_pairs(input_list):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    # make an empty dictionary bc yay dictionaries
    pair_zero = {}

    copy_of_input_list = input_list[:]

    # iterate over each number in our list
    # then have a nested for loop doing the same, with a copy of our input list
    # if the number from the outside loop + the number from inside loop == 0,
    # add it to our dictionary
    # the dictionary takes care of uniqueness
    for num in input_list:
        for num2 in copy_of_input_list:
            if num + num2 == 0:
                pair_zero[num] = num2

    # convert list of tuples into list of lists, sort each pair
    output_list = []
    for paired_tuple in pair_zero.items():
        paired_list = list(paired_tuple)
        paired_list.sort()
        output_list.append(paired_list)


    # check for duplicates-
    # for each pair, append to our final output list if we don't already have it
    final_output = []
    for pair in output_list:
        if pair not in final_output:
            final_output.append(pair)
    return final_output


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
