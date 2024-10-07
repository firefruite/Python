""" 序列类型
1. 列表 -- 末尾添加/删除元素很快，开头添加/删除元素很慢(所有元素都必须移动一位) -- mutable类型
    添加：无返回值
        append(x) -- a[len(a):] = [x]
        extend(x: iterable) -- a[len(a):] = iterable
        insert(i, x)

    删除：
        remove(x) -- 删除第一个值为x的元素，未找到时，触发ValueError
        pop([i]) -- 移除列表中给定的条目，并返回该条目
        clear() -- del a[:]

    查找：
        index(x[, start[, end]]) -- 返回第一个值为x的元素下表，未找到时，触发ValueError
        count(x) -- 值为x的元素个数

    排序：
        sort(*, key=None, reverse=False) -- 就地排序列表中的元素
        reverse()

    复制：
        copy() -- 浅复制 -- a[:]

2. 列表推导式 -- 生成一个新列表
    [i+1 for i in range(10)]
    方括号内：一个表达式，一个for语句，零个或者多个for/if子句

3. del
    del删除某个变量后，不能再引用

4. 元组 -- immutable类型
    输入时，圆括号可有可无；输出时，元组都要有圆括号标注
        t = 123, 456, 'tuple' -- (123, 456, 'tuple') -- 异质元素
        t = (123, 456, 'tuple')
    空元组：t = tuple() -- t = ()
    ***** 单元素元组：t = 'hello', -- t = ('hello',)

5. 集合 -- mutable类型
    ***** 创建集合使用花括号{}或者set函数，创建空集合只能使用set函数，不能用{}，{}创建的是空字典
    集合推导式
        a = {x for x in 'abracadabra' if x not in 'abc'}

6. 字典 -- 映射类型，不是序列类型
    字典不是按固定范围的数字进行索引，而是按键。键是唯一的，任意不可变类型的对象都可作为键 -- 数字、字符串、元组
        如果元组以直接或间接方式包含了可变类型对象，则不可以再作为键
    {}创建空字典
    list(d) -- 返回字典d中所有键的列表，按插入次序排序(推荐sorted函数排序字典)
    in -- 检查是否存在某个键
    字典推导式
        {x: x**2 for x in (2, 4, 6)}

7. 循坏的技巧
    dict.items()
    enumerate() -- 同时取出位置索引和对应的值
    zip() -- 同时循环多个序列，将其内的元素一一匹配
    reversed() -- 反转序列
    sorted() -- 在不改动原序列的基础上，返回一个新序列

8. 深入条件控制
    in -- not in
    is -- is not -- 检查是否为同一对象
    比较操作：and or not
        and or是短路运算符：从左到右求值，一旦可以确定结果，求值会结束
        ***** 用作普通值而非布尔值时，短路运算符的返回值通常时最后一个求了值的参数
            A = 1, C = 2, B = ''
            A and B and C -- ''

9. 序列和其它类型的比较
    序列对象可以与相同序列类型的其他对象比较。这种比较使用 字典式 顺序：首先，比较前两个对应元素，如果不相等，则可确定比较结果；
    如果相等，则比较之后的两个元素，以此类推，直到其中一个序列结束。如果要比较的两个元素本身是相同类型的序列，则递归地执行字典式顺序比较。
    如果两个序列中所有的对应元素都相等，则两个序列相等。
"""

if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    print(matrix)

    transposed = [[row[i] for row in matrix] for i in range(4)]
    print(transposed)

    # 等价于下面代码块
    transposed = []
    for i in range(4):
        # 以下 3 行实现了嵌套的列表组
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    print(transposed)

    # 等价于下面内置函数使用
    transposed = list(zip(*matrix))
    print(transposed)