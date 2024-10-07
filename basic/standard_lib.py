"""
1. 操作系统接口
    import os

    os.getcwd() -- 获取当前工作目录
    os.chdir() -- 更改当前工作目录
    os.system("mkdirs today") -- 执行命令

    dir() -- 返回模块的全部名称
    help(os) -- 显示os的说明页面

    ***** shutil模块 -- 文件和目录管理任务(挺有用的)
        sutil.copyfile(origin, destination)
        shutil.move(source, destination)

2. 文件通配符
    import glob
    glob.glob('*.py')
    ['primes.py', 'random.py', 'quote.py']

3. 命令行参数
    import os
    os.argv

    argparse模块 -- 经常遇到
    import argparse

    parser = argparse.ArgumentParser(
        prog='top',
        description='Show top lines from each file')
    parser.add_argument('filenames', nargs='+')
    parser.add_argument('-l', '--lines', type=int, default=10)
    args = parser.parse_args()
    print(args)

4. 错误输出重定向与程序终止 -- stdin stdout stderr sys.exit()
    import sys
    sys.stderr.write('Warning, log file not found starting a new one\n')
    # Warning, log file not found starting a new one

5. 字符串匹配模式 -- re模块
6. 数学 -- math模块
7. 互联网访问 -- urllib.request模块
8. 日期和时间 -- datetime模块
9. 数据压缩 -- zlib gzip bz2 lzma zipfile tarfile
    import zlib
    s = b'witch which has which witches wrist watch'
    len(s)
    41
    t = zlib.compress(s)
    len(t)
    37
    zlib.decompress(t)
    b'witch which has which witches wrist watch'
    zlib.crc32(s)
    226805979
10. 性能测量 -- timeit模块
    from timeit import Timer
    Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
    0.57535828626024577
    Timer('a,b = b,a', 'a=1; b=2').timeit()
    0.54962537085770791

    与timeit的精细粒度相反，profile和pstats模块提供了用于在较大代码块中识别时间关键部分的工具

11. 质量控制 -- 单元测试 -- doctest
    doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试
    def average(values):
        请注意，此处是一个文档字符串
        '计算数字列表的算术平均值

        print(average([20, 30, 70]))
        40.0
        '
        return sum(values) / len(values)

    import doctest
    doctest.testmod()   # 自动验证嵌入式测试

    unittest模块在一个独立文件中维护更全面的测试集
    import unittest

    class TestStatisticalFunctions(unittest.TestCase):

        def test_average(self):
            self.assertEqual(average([20, 30, 70]), 40.0)
            self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
            with self.assertRaises(ZeroDivisionError):
                average([])
            with self.assertRaises(TypeError):
                average(20, 30, 70)

    unittest.main()  # 从命令行调用时会执行所有测试

12. json模块 csv模块 -- 支持以逗号分隔值格式直接读取和写入文件
13. 格式化输出 -- reprlib模块 pprint模块
14. 模板 -- string模块有一个Template类
    通过占位符实现格式化，占位符：$ + {Python合法标识符} -- 数字、字母和下划线组成
    from string import Template
    t = Template('${village}folk send $$10 to $cause.')
    t.substitute(village='Nottingham', cause='the ditch fund') # 如果占位符参数没有提供，将触发KeyError

    safe_substitute() # 如果占位符参数没有提供，将原样输出，不触发异常
15. 二进制数据记录格式 -- struct模块
    pack()和unpack()方法
        Pack 代码 "H" 和 "I" 分别代表两字节和四字节无符号整数。"<" 代表它们是标准尺寸的小端字节序

    import struct

    with open('myfile.zip', 'rb') as f:
        data = f.read()

    start = 0
    for i in range(3):                      # 显示前 3 个文件标头
        start += 14
        fields = struct.unpack('<IIIHH', data[start:start+16])
        crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

        start += 16
        filename = data[start:start+filenamesize]
        start += filenamesize
        extra = data[start:start+extra_size]
        print(filename, hex(crc32), comp_size, uncomp_size)

        start += extra_size + comp_size     # 跳过下一个标头
16. 多线程 -- threading模块 -- 适用IO密集型任务
    import threading, zipfile

    class AsyncZip(threading.Thread):
        def __init__(self, infile, outfile):
            threading.Thread.__init__(self)
            self.infile = infile
            self.outfile = outfile

        def run(self):
            f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
            f.write(self.infile)
            f.close()
            print('Finished background zip of:', self.infile)

    background = AsyncZip('mydata.txt', 'myarchive.zip')
    background.start()
    print('The main program continues to run in foreground.')

    background.join()    # 等待背景任务结束
    print('Main program waited until background was done.')

    实现多任务协作的首选方法是将所有对资源的请求集中到一个线程中，然后使用 queue 模块向该线程供应来自其他线程的请求。
    应用程序使用 Queue 对象进行线程间通信和协调，更易于设计，更易读，更可靠。
17. 日志记录 -- logging模块
    debug() info() warning() error() critical()
18. 弱引用
    Python会进行自动内存管理，当某个对象的最后一个引用被移除后不久就会释放其所占用的内存

    import weakref, gc
    class A:
        def __init__(self, value):
            self.value = value
        def __repr__(self):
            return str(self.value)

    a = A(10)                   # create a reference
    d = weakref.WeakValueDictionary()
    d['primary'] = a            # does not create a reference
    d['primary']                # fetch the object if it is still alive
    10
    del a                       # remove the one reference
    gc.collect()                # run garbage collection right away
    0
    d['primary']                # entry was automatically removed
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        d['primary']                # entry was automatically removed
      File "C:/python312/lib/weakref.py", line 46, in __getitem__
        o = self.data[key]()
    KeyError: 'primary'
19. 用于操作列表的工具
    array模块 -- array对象 -- 只能存储单一类型的数据
        from array import array
        a = array('H', [4000, 10, 700, 22222])
    collections模块 -- deque对象 -- 从左端添加和弹出的速度较快而在中间查找的速度较慢
    bisect模块
    heapq模块 -- 基于常规列表来实现堆的函数，最小值的条目总是保持在位置零。
"""


import queue
import threading

# 创建一个队列用于存储请求
request_queue = queue.Queue()

# 主线程函数，从队列中获取请求并处理
def main_thread_func():
    while True:
        request = request_queue.get() # 获取队列中的请求
        if request is None: # 如果收到None，则表示停止
            break
        print(f"Processing {request}")
        request_queue.task_done() # 处理完一个请求

# 创建主线程
main_thread = threading.Thread(target=main_thread_func)
main_thread.start()

# 辅助线程，向队列中添加请求
def worker_thread_func(thread_name, requests):
    for request in requests:
        print(f"{thread_name} adding {request} to the queue")
        request_queue.put(request) # 向队列中添加请求
    request_queue.join() # 等待所有请求被处理完毕

# 创建两个辅助线程，并向队列中添加请求
worker1 = threading.Thread(target=worker_thread_func, args=("Worker 1", ["task1", "task2"]))
worker2 = threading.Thread(target=worker_thread_func, args=("Worker 2", ["task3", "task4"]))

worker1.start()
worker2.start()

worker1.join()
worker2.join()

# 停止主线程
request_queue.put(None)
main_thread.join()

print("All tasks done.")