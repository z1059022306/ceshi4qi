"""
    字典的定义
    dictionary（字典） 是 除列表以外 Python 之中 最灵活 的数据类型
    字典同样可以用来 存储多个数据
    通常用于存储 描述一个 物体 的相关信息
    字典用 {} 定义
    字典使用 键值对 存储数据，键值对之间使用 , 分隔
    键 key 是索引
    值 value 是数据
    键 和 值 之间使用 : 分隔
    值 可以取任何数据类型，但 键 只能使用 字符串、数字或 元组
    键必须是唯一的
"""
# 定义字典
xiaoming = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75}

# 取出元素的值
print(xiaoming["name"])  # 输出： 小明

"""
    1	增加	字典[键] = 数据	键不存在，会添加键值对；键存在，会修改键值对的值
    2	删除	del 字典[键]	删除指定的键值对
        字典.pop(键)	删除指定键值对,返回被删除的值
        字典.clear	清空字典
    3	修改	字典[键] = 数据	键不存在，会添加键值对；键存在，会修改键值对的值
        字典.setdefault(键，数据)	键值对不存在，添加键值对；存在则不做处理
        字典.update(字典2)	取出字典2的键值对，键值对不存在，添加键值对；存在则修改值
    4	查询	字典[键]	根据键取值，键值对不存在会报错
        字典.get(键)	根据键取值，键值对不存在不会报错
        字典.keys()	可进行遍历，获取所有键
        字典.values()	可进行遍历，获取所有值
        字典.items()	可进行遍历，获取所有(键，值)
    5	遍历	for key in 字典	取出元组中的每个元素的 key
"""

