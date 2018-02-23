

goodlists =[('a', 820),
            ('b', 83300),
            ('c', 2810),
            ('d', 200),
            ('e', 130),
            ('f', 600),
            ('g', 220),
            ]
shopping = list()
money = input('请输入您的余额：')
if money.isdigit():
    money = int(money)
    while True:
        for index,i in enumerate(goodlists):
            print(index,i)
        chooseItem = input('请选择商品编号：')
        if chooseItem.isdigit():
            chooseItem = int(chooseItem)

            if 0 <= chooseItem and chooseItem < len(goodlists):
                p_itme = goodlists[chooseItem][0]
                shopping.append(p_itme)
                money = money - goodlists[chooseItem][1]
                if money > 0:
                    print('您选择了%s,当前余额是\033[31;1m%d\033[0m' % (shopping,money))
                else:
                    print('\033[31;1m余额位%d\033[0m'% money)
            else:
                print('输入编号不存在')

        elif chooseItem =='p':
            print('购物结束，您的购物车有%s,余额%d' %(shopping,money))
            exit()
        else:
            print('请输入正确编号')
else:
    print('输入金额有误！')
