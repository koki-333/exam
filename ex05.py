list_num = [13, 17, 31, 57, '', 41, 83]

def remove_empty(list_num):
	newList_num = []

	for i in list_num:
		if i != '':
			newList_num.append(i)

	return newList_num


def list_avarage(list_num):
	num = 0
	for i in list_num:
		num += i

	num_ava = num/len(list_num)
	return  num_ava

newList_num = remove_empty(list_num)
print(newList_num)
num_ava = list_avarage(newList_num)

print(f'平均値: {num_ava}')