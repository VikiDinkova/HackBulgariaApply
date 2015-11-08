def word_game(word, table):
	count = 0
	for row in table:
		row = ''.join(row)
		# If word is palindrom
		if row == word and row[::-1] == word:
			count += 2
		elif row == word or row[::-1] == word:
			count += 1
	diagonal = []

	for row_index in range(len(table)):
		for element_index in range(len(table[0])):
			if row_index == element_index:
				diagonal.append(table[row_index][element_index])
	diagonal = ''.join(diagonal)
	if diagonal == word and diagonal[::-1] == word:
		count += 2
	elif diagonal == word or diagonal[::-1] == word:
		count += 1

	for col in range(len(table[0])):
		column = []
		for el_in_col in range(len(table)):
			column.append(table[el_in_col][col])
		column = ''.join(column)
		if word in column and word in column[::-1]:
			count += 2
		elif word in column or word in column[::-1]:
			count += 1	
	return count


table = [['i', 'v', 'a', 'n'], ['e', 'v', 'n', 'h'], ['i', 'n','a', 'v'], ['m', 'v', 'v', 'n'], ['q', 'r', 'i', 't']]
table2 = [['i', 'i', 'i', 'i'], ['i', 'v', 'n', 'h'], ['i', 'n','a', 'v'], ['i', 'v', 'v', 'n'], ['q', 'r', 'i', 't']]
word = 'ivan'
word2 = 'iiii'
print(word_game(word, table))
print(word_game(word2, table2))
