def point(x, y, directions):
	direction = 1
	for direct in directions:
		if direct == '>':
			x += direction
		elif direct == '<':
			x -= direction
		elif direct == '^':
			y -= direction
		elif direct == 'v':
			y += direction
		elif direct == '~':
			direction *= -1
			
	return (x, y)


x = 0
y = 0
directions = '>>><<<~>>>~^^^'
print(point(x, y, directions))