def get_duplicate_indices(words):
	"""Given a list of words, loop through the words and check for each
	   word if it occurs more than once.
	   If so return the index of its first ocurrence.
	   For example in the following list 'is' and 'it'
	   occurr more than once, and they are at indices 0 and 1 so you would
	   return [0, 1]:
	   ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
	   Make sure the returning list is unique and sorted in ascending order."""
	# one way
	# dups_indices_lst = []
	# sort_set_lst = sorted(set(words), key=lambda x: words.index(x))

	# for word in sort_set_lst:
	#     if words.count(word) > 1:
	#         r = words.index(word)
	#         dups_indices_lst.append(r)
	# return dups_indices_lst

	# another way
	duplicate_set = {word for word in words if words.count(word) > 1}
	result = sorted([words.index(word) for word in duplicate_set])
	return result


# tests
def test_get_duplicate_indices_docstring():
	words = ['is', 'it', 'true', 'or', 'is', 'it', 'not']
	assert get_duplicate_indices(words) == [0, 1]


def test_get_duplicate_indices_bite_text():
	words = ['this', 'is', 'a', 'new', 'bite', 'I', 'hope', 'this',
			 'bite', 'will', 'teach', 'you', 'something', 'new']
	assert get_duplicate_indices(words) == [0, 3, 4]


def test_get_duplicate_indices_another_text():
	# keeping it simple with split on space, so lists != lists.
	words = ('List comprehensions provide a concise way to create '
			 'lists. Common applications are to make new lists where '
			 'each element is the result of some operations applied '
			 'to each member of another sequence or iterable, or to '
			 'create a subsequence of those elements that satisfy a '
			 'certain condition').split()
	assert get_duplicate_indices(words) == [3, 6, 7, 17, 22, 32]