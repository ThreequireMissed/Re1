'''逆转字符串——输入一个字符串，将其逆转并输出。2018-1-31'''
str = input("输入一个字符串：")
rts = ''
n = len(str)
for i in range(-1,-n-1,-1):
    rts += str[i]
    print(i)
print("逆转得到：",rts)



