def reverse_words_in_str(s):

	return ' '.join([word[::-1] for word in s.split()])

sentence = "This is a good day"
rev_res = reverse_words_in_str(sentence)
print rev_res