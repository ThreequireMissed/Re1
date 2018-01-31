'''判断是否为回文——判断用户输入的字符串是否为回文。
回文是指正反拼写形式都是一样的词，譬如“racecar”。'''
str = input("输入一个字符串吧：")
for i in range(len(str)):
    if str[i] != str[-i-1]:
        print(str,"不是回文")
        break
    elif i == len(str)/2:
        print(str,"是回文")
    else:
        pass
