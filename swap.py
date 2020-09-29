def swap(array, index1, index2):
    # swap it!
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp


def compare(item1, item2):
    # this compares dictionaries!
    return item1['count'] > item2['count']


def sort(array):
    # this is our sort
    for n in range(len(array)):
        for index in range(len(array) - 1):
            if compare(array[index], array[index + 1]):
                swap(array, index, index + 1)
    return array


array = [
    {
        'result': 'I\'m not typing 123 yays!',
        'count': 123,
    },
    {
        'result': 'Elizabeth yay yay yay yay!',
        'count': 4,
    },
    {
        'result': 'Yay Elizabeth!',
        'count': 1,
    },
]

# array = ['hi', 'hahahahahahahahahahahahaha', 'apple', 'banana', 'pie', 'granola', 'rutabega', 'microwave']
#
print(sort(array))
