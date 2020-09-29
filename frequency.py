# def frequency_count(query, to_search):
#     """Get frequncy for a sentence"""
#     frequency = 0
#
#     for search_word in to_search.lower().split():
#         if query in search_word:
#             # we have a match!
#             frequency += 1
#
#     print("frequency is", frequency)
#     return frequency
#
#
# def main():
#     """Run a bunch of tests for our search function"""
#
#     assert frequency_count('elizabeth', 'Elizabeth Elizabeth Elizabeth') == 3
#     assert frequency_count('elizabeth', 'Elizabeth Elizabeth Elizabeth!') == 3
#
#     print('tests pass you rock!!\n\n')
#
#
# main()


input_dict = {"Elizabeth says 'Elizabeth is great!'": 2, 'Elizabeth Gets Straight As Forever': 1, 'Elizabeth Elizabeth Elizabeth!': 3}

print(input_dict)

# sort!
sorted = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)

print(sorted)

output_dict = ['Elizabeth Elizabeth Elizabeth!', "Elizabeth says 'Elizabeth is great!'", 'Elizabeth Gets Straight As Forever']

assert sorted == output_dict
