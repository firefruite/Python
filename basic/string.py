"""
1. 不将\转义成特殊字符，可\\或者原始字符串 -- r+字符串字面值 原始字符串中\的数量只能是偶数(*****)
2. 相邻字符串会自动拼接 -- 只能是字符串字面值，不能是变量或表达式
    'py' 'thon' -- 'python'
    ('py'
    'thon') -- 'python'
    错误: (*****)
    a = 'py'
    a 'thon'
3. + -- 拼接字符串  * -- 重复字符串(序列)
4. 切片理解
     +---+---+---+---+---+---+
     | P | y | t | h | o | n |
     +---+---+---+---+---+---+
     0   1   2   3   4   5   6
    -6  -5  -4  -3  -2  -1
5. 字符串不能修改，元素的赋值操作将抛出异常
6. f字符串
7. 格式化字符串: 花括号{}括起来的'替换字符'，花括号外的内容被视为字面文本
    - 格式化字符串字面值 -- f字符串
    - format函数
        str.format()

        "First, thou shalt count to {0}"  # 引用第一个位置参数
        "Bring me a {}"                   # 隐式引用第一个位置参数
        "From {} to {}"                   # 等同于 "From {0} to {1}"
        "My quest is {name}"              # 引用关键字参数 'name'
        "Weight in tons {0.weight}"       # 第一个位置参数的 'weight' 属性
        "Units destroyed: {players[0]}"   # 关键字参数 'players' 的第一个元素。

        "Harold's a clever {0!s}"        # 先在参数上调用 str()
        "Bring out the holy {name!r}"    # 先在参数上调用 repr()
        "More {!a}"                      # 先在参数上调用 ascii()

        最好是使用名称来引用变量，可以直接传入字典
    - 手动格式化字符串 -- 使用一些格式化的函数，填充空格函数等
    - 旧式字符串格式化 -- printf风格
        print('The value of pi is approximately %5.3f.' % math.pi)
8. 单引号和双引号的唯一区别：单引号里无法对双引号转义，反之亦然
9. str()和repr()函数
    str() -- 供人类阅读的字符串形式
    repr() -- 适于解释器解释的字符串形式
"""

if __name__ == "__main__":
    a = ('con'
         "c"
         'at')
    print(a)
