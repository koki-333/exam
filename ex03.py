input_mail = input('メールアドレスを入力してください:')

def domein(input_mail):
	spStr = input_mail.split('@')

	print(f'メールアドレス( {input_mail} )のドメイン: {spStr[1]}')

domein(input_mail)