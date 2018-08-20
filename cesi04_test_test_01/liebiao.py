name_list = ["zhangsan", "lisi", "wangwu"]
# 取出列表中元素的值
print(name_list[1])  # 输出 lisi

# 列表常用操作
"""
    1	增加	列表.append(数据)	在末尾追加数据
        列表.insert(索引, 数据)	在指定位置插入数据(位置前有空元素会补位)
        列表.extend(Iterable)	将可迭代对象中 的元素 追加到列表
    2	删除	del 列表[索引]	删除指定索引的数据
        列表.remove(数据)	删除第一个出现的指定数据
        列表.pop()	删除末尾数据,返回被删除的元素
        列表.pop(索引)	删除指定索引数据
        列表.clear	清空列表
    3	修改	列表[索引] = 数据	修改指定索引的数据，数据不存在会报错
    4	查询	列表[索引]	根据索引取值，索引不存在会报错
        列表.index(数据)	根据值查询索引，返回首次出现时的索引，没有查到会报错
        列表.count(数据)	数据在列表中出现的次数
        len(列表)	列表长度
        if 数据 in 列表:	检查列表中是否包含某元素
    5	排序	列表.sort()	升序排序
        列表.sort(reverse=True)	降序排序
        列表.reverse()	逆序、反转
"""
# 列表 增
my_list = [111, 222, 333]
my_list.append(444)
my_list.append(555)
my_list.append(666)
my_list.append(777)
print(my_list)
# 列表 删

# del my_list[1]
# print(my_list)

# 列表 改
# my_list[2]=2421
# print(my_list)

# 列表 查
print(my_list[4])
# 用for循环进行遍历
for i in my_list:
    print(i)

# 列表 嵌套
"""
    类似while循环的嵌套，列表也是支持嵌套的
    一个列表中的元素又是一个列表，那么这就是列表的嵌套
"""

# 一个学校，有3个办公室，现在有8位老师等待工位的分配，
# 请编写程序: 1> 完成随机的分配 2> 获取办公室信息 (每个办公室中的人数，及分别是谁)


import random

# 定义一个列表用来保存3个办公室
offices = [[], [], []]

# 定义一个列表用来存储8位老师的名字
names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# 完成随机分配
i = 0
for name in names:
    index = random.randint(0, 2)
    offices[index].append(name)

# 获取办公室信息
i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d' % (i, len(tempNames)))
    i += 1
    for name in tempNames:
        print("%s" % name, end='')
    print("\n")
    print("-" * 20)
