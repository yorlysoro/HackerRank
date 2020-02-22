def second_lower_grade(nested_list):
	second_list = list()
	order_list = list()
	for i in range(len(nested_list)):
		if i != 0:
			try:
				if nested_list[i][1] <= nested_list[i-1][1] and len(second_list) < 5:
					second_list.append([nested_list[i][0], nested_list[i][1]])
			except IndexError as ie:
				print(ie)
		else:
			second_list.append([nested_list[i][0], nested_list[i][1]])
	for i in range(len(second_list)):
		order_list.append(second_list[i][0])


	return sorted(order_list, key=str.lower)

if __name__ == '__main__':
	nested_list = list()
	for i in range(int(input())):
		name = input()
		score = float(input())
		nested_list.append([name, score])
	print(nested_list)
	seconds = second_lower_grade(nested_list)
	print(seconds)

