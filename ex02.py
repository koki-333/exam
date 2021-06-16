input_mail = input('メールアドレスを入力してください:')

def check_addres(addres):
	check_num = 0
	check_at = 0
	for str in addres:
		if str == '@':
			check_at += 1

		if str == '@':
			if check_num == 0:
				print('何かおかしいです')
				break
			elif check_num == len(addres):
				print('何かおかしいです')
				break

		if check_at == 2:
			print('何かおかしいです')
			break

		check_num += 1
		if check_num == len(addres):
			if check_at == 0:
				print('何かおかしいです')
				break
			else:
				print('正しいメールアドレスです')


check_addres(input_mail)