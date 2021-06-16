input_id = input('IDを入力してください: ')
input_pass = input('パスワードを入力してください: ')

#ID = ootsubo  pass = English

def check_id(id, password):
	idPass = ['ootsubo', 'English']
	if id == idPass[0]:
		if password == idPass[1]:
			print('OKです')
		else:
			print('IDかパスワードが違います')
	else:
		print('IDかパスワードが違います')

check_id(input_id, input_pass)