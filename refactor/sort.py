

def compare(item1, item2):
    return item1['count'] < item2['count']


def swap(array, index1, index2):
    tmp = array[index1]
    array[index1] = array[index2]
    array[index2] = tmp


def sort(array):
    """Sort an array of numbers! We will use bubble sort"""
    length = len(array)

    for pass_number in range(length):
        for index in range(length - 1):
            if compare(array[index], array[index + 1]):
                swap(array, index, index+1)

    return array
