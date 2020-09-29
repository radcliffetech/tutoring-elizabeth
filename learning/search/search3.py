"""

Super awesome search tool!

TODO:

# fix tests!
# add most relevant returns first - how do we do this?

"""

# this is our test selection of story headlines
data = [
   "Elizabeth says 'Elizabeth is great!'",
   "Elizabeth Gets Straight As Forever",
   "Jeffrey drinks too much coffee!",
   "Elizabeth gets attacked by a massive hippopotamus",
   "Jeffrey achieves world record of no sleep for 4 weeks",
   "Elizabeth outruns world's fastest cheetah",
   "Hannah is in high school and is too busy to learn CS",
   "Jeffrey gives too much homework. Boo.",
   "Elizabeth Elizabeth Elizabeth!",
]


def frequency_count(query, to_search):
    """Get frequncy for a sentence"""
    frequency = 0

    for search_word in to_search.lower().split():
        if query in search_word:
            # we have a match!
            frequency += 1

    print("frequency is", frequency)
    return frequency


def search(query):
    """Take a search string and search our data!

    Query can be any number of words long, yeah!
    """

    query = query.lower()

    words_in_query = query.split()

    matched_results = []
    results_dict = {}

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
            matched_results.append(original_name)
            results_dict[original_name] = frequency

    print(results_dict)

    return matched_results, len(matched_results)


def main():

    """Run a bunch of tests for our search function"""

    matched_results, search_count = search("hannah")
    assert matched_results == ["Hannah is in high school and is too busy to learn CS"]
    assert search_count == 1

    matched_results, search_count = search("Elizabeth")
    assert search_count == 5

    # rewrite these to pass
    matched_results, search_count = search("hannah")
    assert search_count == 1

    matched_results, search_count = search("Jeffrey world sleep")
    assert search_count == 1

    matched_results, search_count = search("dragon")
    assert search_count == 0

    matched_results, search_count = search("Elizabeth")
    assert search_count == 5
    assert matched_results[0] == "Elizabeth Elizabeth Elizabeth!"
    assert matched_results[1] == "Elizabeth says 'Elizabeth is great!'"

    print('tests pass you rock!!\n\n')


main()
