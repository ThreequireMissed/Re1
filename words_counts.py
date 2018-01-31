'''统计字符串中的单词数目——统计字符串中单词的数目，
更复杂的话从一个文本中读出字符串并生成单词数目统计结果。'''
file_path = input("请输入文件路径：")
counts_info = {}
with open(file_path) as f:
    rules = str.maketrans(',:-."\n', '      ')
    word = f.read().translate(rules)
    word_list = word.split(' ')
    while '' in word_list:
        word_list.remove('')
    for i in set(word_list):
        counts_info[i] = word_list.count(i)
    f.close()
print("文本内共有单词数量%d个"%sum(counts_info.values()))
for x in counts_info.items():
    print('单词%s出现%d次'%x)







