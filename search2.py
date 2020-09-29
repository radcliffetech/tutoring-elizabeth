data = [
    "Elizabeth Gets Straight As Forever",
    "Jeffrey drinks too much coffee!",
    "Elizabeth gets attacked by a massive hippopotamus",
    "Jeffrey achieves world record of no sleep for 4 weeks",
    "Elizabeth outruns world's fastest cheetah"
]


def search(query):
    """Take a keyword and search!

    Query can be one or two words.
    """

    search_count = 0
    query = query.lower()

    word_list = query.split()

    # this is the number of matches we need to hit!
    matches_required = len(word_list)
    
    for index in range(len(data)):
        search_name = data[index].lower()

        # look to see if the query is found
        # NEW LOOP
        match = False


        for word in word_list:
            if word in search_name:
                # do something here to make it work
                pass
        if match is True:
            search_count = search_count + 1

    print("Returning", search_count)
    return search_count


def main():
    assert search("Elizabeth") == 3
    assert search("Elizabeth cheetah") == 1

    assert search('Dragon') == 0

    print('tests pass!')


main()
