import re


def isUserName(username):
	res = re.findall(r"^[a-zA-Z]\w{3,15}$",username)#4-16位，以字母开头的字母数字下划线
	if res:
		return True
	else:
		return False

def isPassWord(password):
	res = re.findall(r"^[^\u4E00-\u9FA5]{6,20}$",password) #除中文外的任意6-20个字符
	if res:
		return True
	else:
		return False


