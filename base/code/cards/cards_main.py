#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :
@Contact :   1119405009@qq.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/21 10:33   felix      1.0         None
'''
# import lib
#!/usr/bin/python3

from  base.code.cards.cards_tools import *;
while True:

    show_menu()

    action = input("请选择操作功能：")

    print("您选择的操作是：%s" % action)

    # 根据用户输入决定后续的操作
    if action in ["1", "2", "3"]:

        if action == "1":
            new_card()

        elif action == "2":
           show_all()

        elif action == "3":
            search_card()

    elif action == "0":
        print("欢迎再次使用【名片管理系统】")

        break
    else:
        print("输入错误，请重新输入：")
