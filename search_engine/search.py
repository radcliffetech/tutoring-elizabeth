from sort import sort
from search_data import data


def frequency_count(query, to_search):
    """Get frequency for a sentence"""
    frequency = 0

    for search_word in to_search.lower().split():
        if query in search_word:
            # we have a match!
            frequency += 1

    return frequency


def search(query):
    """Take a search string and search our data!

    Query can be any number of words long, yeah!
    """

    query = query.lower()

    words_in_query = query.split()

    matched_results = []

    # loop through our data and look for matches!
    for index in range(len(data)):
        search_name = data[index].lower()
        original_name = data[index]

        # this is for multiple keywords
        total_matches = 0

        frequency = frequency_count(query, search_name)

        for query_word in words_in_query:

            if query_word in search_name:
                # how many times does it match?
                total_matches += 1

        # must match all words in query to count as a match!
        if total_matches == len(words_in_query):
            match_dict = {
                'result': original_name,
                'count': frequency,
            }
            matched_results.append(match_dict)

    sort(matched_results)
    return matched_results
