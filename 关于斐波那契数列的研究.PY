# 关于斐波那契数列的研究

# 斐波那契数列
# 1  1  2  3  5  8  13  21  34  55  89  144  以此类推

# 数学抽象
# 设斐波那契数列为f(n)
# 显然斐波那契数列满足以下两个条件
# 当n = 1或n = 2时,f(n) = 1
# 当n > 2时,f(n) = f(n - 1) + f(n - 2)

# 代码实现(仅仅提供三种解法)
# 方法一:函数递归
# def f(num):
#     if num == 1 or num == 2:
#         return 1
#     else:
#         return f(num - 1) + f(num - 2)
#
#
# n = int(input("请输入你要查看斐波那契数列的项数:"))
# print(f"斐波那契数列的第{n}项为{f(n)}")
#
# # 方法二:列表
# li_f = [1, 1]
# user_num1 = int(input("请输入你要查看斐波那契数列的项数:"))
# for i in range(user_num1 - 2):
#     num_new = li_f[-1] + li_f[-2]
#     li_f.append(num_new)
# print(f"斐波那契数列的第{user_num1}项为{li_f[-1]}")

# 根据斐波那契数列的递推式,得到斐波那契数列的特征方程,解方程,易得斐波那契数列的通式
# 方法三:公式
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

