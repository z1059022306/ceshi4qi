"""
    4.1 字符串的定义
    字符串 就是 一串字符，是编程语言中表示文本的数据类型
    在 Python 中可以使用 一对双引号 " 或者 一对单引号 ' 定义一个字符串
    虽然可以使用 \" 或者 \' 做字符串的转义，但是在实际开发中：
    如果字符串内部需要使用 "，可以使用 ' 定义字符串
    如果字符串内部需要使用 '，可以使用 " 定义字符串
    可以使用 索引 获取一个字符串中 指定位置的字符，索引计数从 0 开始
    也可以使用 for 循环遍历 字符串中每一个字符
"""
string = "hello world"
# 用for循环遍历字符串中的字符
for i in string:
    print(i)
# 字符串的操作
# 1.判断
# 判断字符是否全部都是字母（是则返回True ,不是返回False）
if_zimu = string.isalpha()
print(if_zimu)
# 判断字符是否全部都是数字（是则返回True ,不是返回False）
if_int = string.isdecimal()
print(if_int)
# 2.查找和替换
"""
    string.find(str, start=0, end=len(string))
    检测 str 是否包含在 string 中，
    如果 start 和 end 指定范围，则检查是否包含在指定范围内，
    如果是返回开始的索引值，否则返回 -1
"""
# 查找"l"在索引0-5中
a = string.find("l", 0, 5)
print(a)
"""
    string.replace(old_str, new_str, num=string.count(old))
    返回一个新字符串，把 string 中的 old_str 替换成 new_str，如果 num 指定，则替换不超过 num 次
"""
# 将原字符串中的“l”替换成“L”，返回新的字符串
new_string = string.replace("l", "L")
print(new_string)
print(string)
# 3.拆分和链接
"""
    string.partition(str)
    返回元组，把字符串 string 分成一个 3 元素的元组 (str前面, str, str后面)
"""
# 将字符串string按照“w"分成三个元素的元组
b = string.partition("w")
print("b=", b)
"""
string.split(str="", num)
返回列表，以 str 为分隔符拆分 string，如果 num 有指定值，
则仅分隔 num + 1 个子字符串，str 默认包含 '\r', '\t', '\n' 和空格
"""
# 将string拆分成多个子串，以列表方式返回
c = string.split("l")
print("c=", c)
d = string.split(" ")
print("d=", d)
"""
    string1 + string2
    字符串拼接
"""
# 字符串拼接
string1 = "hhh"
string2 = "aaa"
new_string1 = string1 + string2
print("new_string1=", new_string1)
# 4.大小写转换
"""
    string.lower()	返回新字符串，转换 string 中所有大写字符为小写
    string.upper()	返回新字符串，转换 string 中的小写字母为大写
"""
big_string = string.upper()
smo_string = new_string.lower()
print("big_string=", big_string)
print("smo_string=", smo_string)

# 字符串切片
"""
    切片 译自英文单词 slice，翻译成另一个解释更好理解: 一部分
    切片 使用 索引值 来限定范围，根据 步长 从原序列中 取出一部分 元素组成新序列
    切片 方法适用于 字符串、列表、元组
"""
"""
    注意：
    
    1.指定的区间属于 左闭右开 型 [开始索引, 结束索引) 对应 开始索引 <= 范围 < 结束索引
    2.从 起始 位开始，到 结束位的前一位 结束（不包含结束位本身)
    3.从头开始，开始索引 数字可以省略，冒号不能省略
    4.到末尾结束，结束索引 数字和冒号都可以省略
    5.步长默认为 1，如果元素连续，数字和冒号都可以省略
"""
"""
    截取从 2 ~ 5 位置 的字符串
    截取从 2 ~ 末尾 的字符串
    截取从 开始 ~ 5 位置 的字符串
    截取完整的字符串
    从开始位置，每隔一个字符截取字符串
    从索引 1 开始，每隔一个取一个
    截取从 2 ~ 末尾 - 1 的字符串
    截取字符串末尾两个字符
    字符串的逆序（面试题）
"""
num_str = "0123456789"

# 1. 截取从 2 ~ 5 位置 的字符串
print(num_str[2:6])

# 2. 截取从 2 ~ `末尾` 的字符串
print(num_str[2:])

# 3. 截取从 `开始` ~ 5 位置 的字符串
print(num_str[:6])

# 4. 截取完整的字符串
print(num_str[:])

# 5. 从开始位置，每隔一个字符截取字符串
print(num_str[::2])

# 6. 从索引 1 开始，每隔一个取一个
print(num_str[1::2])

# 倒序切片
# -1 表示倒数第一个字符
print(num_str[-1])

# 7. 截取从 2 ~ `末尾 - 1` 的字符串
print(num_str[2:-1])

# 8. 截取字符串末尾两个字符
print(num_str[-2:])

# 9. 字符串的逆序（面试题）
print(num_str[::-1])