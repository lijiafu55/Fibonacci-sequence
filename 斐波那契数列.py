a = True #退出条件
user_num2 = 0  #计数器
list_01 = list()  #空列表
while a:
    print(f"你要查看斐波那契数列的项数:{user_num2}")
    f_num = (1 / (5 ** 0.5)) * (((1 + 5 ** 0.5) / 2) ** user_num2 - ((1 - 5 ** 0.5) / 2) ** user_num2)
    print(f"斐波那契数列的第{user_num2}项为{int(f_num)}")
    user_num2 += 1
    list_01.append(int(f_num))
    # print(list_01) #要每项添加就查看列表就可以打开这个
    if user_num2 == 200: #一次查看200-1个斐波那契数列
        a = False
print(list_01)
