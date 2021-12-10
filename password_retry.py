password = 'a123456'
i = 2
while i > -1:
	trial = input('請輸入密碼: ')
	if trial == password:
		print('登入成功')
		break
	elif i == 0:
		print('密碼錯誤! 機會已用完')
		break
	else:
		print('密碼錯誤! 還有', i, '次機會!')
		i = i - 1
