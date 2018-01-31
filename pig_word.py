'''拉丁猪文字游戏——这是一个英语语言游戏。基本规则是将一个英语单词的
第一个辅音音素的字母移动到词尾并且加上后缀-ay（譬如“banana”会变成
“anana-bay”）。'''

str = input("输入一个英语单词吧：")
vowel = 'aeiou'
for i in str:
    if i not in vowel:
        n = str.index(i)
        str = str[:n]+str[n+1:]+i+'ay'
        print("猪式变换后得到：",str)
        break
    else:
        pass