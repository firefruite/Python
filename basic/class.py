"""
1. 作用域和命名空间 -- 作用域可理解为，等价于命名空间
    命名空间 -- 名称到对象的映射
        不同命名空间中的名称之间绝对没有关系

    点号之后的名称是属性，modname.funcname中，modname是模块对象，funcname是模块的属性，
    模块属性和模块内定义的全局名称具有直接的映射关系：共享相同的命名空间

    命名空间动态创建
        内置名称的命名空间在解释器启动式创建，不会删除；
        模块的全局命名空间在读取时创建，解释器退出时删除；
        函数的命名空间在调用时创建，返回或者遇到未处理异常时删除；每次递归都有自己的命名空间

    作用域 -- 命名空间中Python代码的一段文本区域
        ***** 特点：静态创建，动态使用
            代码执行期间，都有3或4个"命名空间可直接访问"嵌套作用域 -- 对用于function.py中描述的变量符号表 *****
                - 最内层作用域，包含局部变量，并首先在其中进行搜索
                - 外层闭包函数作用域，包含"非局部、非全局"的名称，从最靠内层的那个作用域开始，逐层向外搜索
                - 倒数第二层作用域，包含当前模块的全局名称
                - 最外层的作用域，是内置名称的命名空间

        要重新绑定在最内层作用域以外找到的变量，可以使用nonlocal语句；
        如果未使用 nonlocal 声明，这些变量将为只读（尝试写入这样的变量将在最内层作用域中创建一个新的局部变量，而使得同名的外部变量保持不变）。

        ***** 赋值不会复制数据，只是将名称绑定到对象，删除也是如此

        ***** global语句用于表明特定变量在全局作用域中，并应在全局作用域中重新绑定；
              nonlocal语句用于表明特定变量在外层作用域中，并应在外层作用域中重新绑定。

2. 类定义
    class ClassName(BaseClass):
        ...

3. 类对象 -- 支持属性引用 + 实例化
4. 实例对象 -- 支持属性引用
5. 方法对象
    class Complex:
        def __init__(self, realpart, imagpart):
            self.r = realpart
            self.i = imagpart

        def f(self):
            ...

    x = Complex(1, 2) #  实例对象
    xf = x.f() #  方法对象

6. 类和实例变量
    实例变量是每个实例的唯一数据，类变量是类的每个实例公有的属性和方法
    ***** 如果同样的属性同时出现在实例和类中，属性查找优先选择实例

7. 继承
    ***** 派生类可能会重写基类的方法。因为方法在调用同一对象的其他方法时没有特殊权限，所以基类方法在尝试调用同一基类中定义的方法时，
    有可能调用的是该基类的派生类中定义的方法

    isinstance() -- 检查一个实例的类型
    issubclass() -- 检查类的继承关系

    多继承
        class ClassName(Base1, Base2, Base2):
            ...

        属性查询顺序：深度优先，从左到右 *****
            果某个属性在 ClassName 中找不到，就会在 Base1 中搜索它，然后（递归地）在 Base1 的基类中搜索，
            如果在那里也找不到，就将在 Base2 中搜索，依此类推。

8. 私有变量
    Python中不存在"私有"部分
    约定：
        以下划线开头的名称被当作为非公有部分 -- 保护权限 or 私有权限
        名称改写：
            任何形式为__spam的标识符(至少带有两个前缀下划线，至多一个后缀下划线)将被替换为_classname__spam

            class Mapping:
                def __init__(self, iterable):
                    self.items_list = []
                    self.__update(iterable)

                def update(self, iterable):
                    for item in iterable:
                        self.items_list.append(item)

                __update = update   # 原始 update() 方法的私有副本

            class MappingSubclass(Mapping):

                def update(self, keys, values):
                    # 为 update() 提供了新的签名
                    # 但不会破坏 __init__()
                    for item in zip(keys, values):
                        self.items_list.append(item)

        getattr() setattr() delattr()

9. 数据模型
    from dataclasses import dataclass

    # Pydantic对象
    @dataclass
    class Employee:
        name: str
        dept: str
        salary: int

10. 迭代器
        实现了__next__()方法的方法
        iter() -- 返回一个迭代器
        next() -- 返回下一个值，越界触发StopIteration异常

        ***** 迭代器协议：定义了__next__()方法，__iter__()返回一个__next__()方法
            class Reverse:
                # 对一个序列执行反向循环的迭代器。
                def __init__(self, data):
                    self.data = data
                    self.index = len(data)

                def __iter__(self):
                    # 如果类已经定义了__next__()方法，__iter__()只需返回self
                    return self

                def __next__(self):
                    if self.index == 0:
                        raise StopIteration
                    self.index = self.index - 1
                    return self.data[self.index]

11. 生成器
        包含yield语句

        # 生成器协议
        def reverse(data):
            for index in range(len(data)-1, -1, -1):
                yield data[index]

        自动创建__iter__()和__next__()方法，每次调用时会自动保存变量状态

        next() -- 返回下一个值，越界触发StopIteration异常
"""


# 作用域和命名空间的示例
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)