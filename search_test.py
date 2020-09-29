
animals = [
  'Otter',
  'Dolphin',
  'Cheetah',
  'Monkey',
  'Orangutan',
  'Orca',
  'Bear',
  'Bear Cub',
]


def search(keyword):
    """Take a keyword and search!"""

    search_count = 0
    query = keyword.lower()

    for index in range(len(animals)):
        animal_name = animals[index].lower()

        if query in animal_name:
            search_count = search_count + 1

    return search_count


def main():
    assert search("Bear's") == 2
    assert search('bear') == 2
    assert search('bear cub') == 1
    assert search('or') == 2

    assert search('ear') == 2

    assert search('Orca') == 1
    assert search('Dragon') == 0

    print('tests pass!')


main()
