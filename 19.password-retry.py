"""

題目：密碼重試程式

1.先在程式碼中，設定好密碼password = 'a123456'
2.讓使用者重複輸入密碼
3.最多輸入3次密碼
4.對的話，就印出"登入成功"
5.不對的話，就印出"密碼錯誤"!還有__次機會

"""
x = 3
while x > 0 :
	password = input("請輸入密碼： ")
	if password == "a123456":
		print("登入成功")
		break
	else:
		if x == 1:
			break
		print("密碼錯誤，還有", x - 1, "次機會")
		x = x - 1


