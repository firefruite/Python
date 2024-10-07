"""
1. 模块 -- 包含函数定义和可执行语句的文件
    每次解释器会话中，模块仅导入一次，如果模块内容修改，需要重新导入模块
    ***** 导入模块时，以下划线开头的名称不会导入

2. 模块搜素路径
    导入spam.py模块时，
    搜索具有该模块名称的内置模块 -- sys.builtin_module_names中列出，没有时下一步
        |
    sys.path列表中搜索名为spam.py的文件
            |
        被执行文件所在目录
            |
        PYTHONPATH
            |
        site-packages目录

3. '已编译的'Python文件
    为了加快模块导入，会将python文件的编译版本(module.version.pyc, __pycache__/spam.python-33.pyc)缓存在__pycache__目录中
    编译版本与平台无关

4. 标准模块(builtin) -- Python自带的
    sys.ps1 -- 主提示符
    sys.ps2 -- 辅助提示符
    dir() -- 查找模块 定义 的名称：变量、模块、函数

5. 包
    使用'带点号模块名'的方式引用 -- A.B -- A是包名，B是变量、函数或模块
    ***** 目录被当作 包 使用，需要__init__.py文件，可以是空文件，也可以执行包的初始化工作或设置__all__变量

    from package import * -- 不会导入所有子模块
    import语句使用惯例：
        1. __init__.py中定义了__all__变量时，__all__就是被导入的模块名列表
            __init__.py中不能定义与模块名重名的名称，否则重名模块不会被导入

            __all__ = [
                "echo",      # 指向 'echo.py' 文件
                "surround",  # 指向 'surround.py' 文件
                "reverse",   # !!! 现在指向 'reverse' 函数 !!!
            ]

            def reverse(msg: str):  # <-- 此名称将覆盖 'reverse.py' 子模块
                return msg[::-1]    #     针对 'from sound.effects import *' 的情况
        2. __init__.py中没有定义__all__变量时，不会导入所有子模块
            确保包被导入，包中定义的任何名称被导入

    相对导入和绝对导入
        绝对导入：from module import name
        相对导入 -- 基于当前模块名，使用前导点号来表示相对导入所涉及的当前包和上级包 -- 主程序必须使用绝对导入(主程序名永远是__main__) *****
            # ... 更上一级
            from . import echo  # . 当前目录
            from .. import formats  # .. 父目录
            from ..filters import equalizer

"""