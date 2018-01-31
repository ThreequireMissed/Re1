'''统计元音字母——输入一个字符串，统计处其中元音字母的数量。
更复杂点的话统计出每个元音字母的数量。'''
vowel = {   'a' : 0,
            'e' : 0,
            'i' : 0,
            'o' : 0,
            'u' : 0   }
str  = input("请输入一串字母：")
for i in str:
    if i in vowel.keys():
        vowel[i] += 1
    else:
        pass
for i in vowel.items():
    print('元音%s出现次数为：%d'%(i))
