"""
1. 异常 -- 包括语法错误和错误
    语法错误，解析错误
    错误，执行时发生的错误

2. 异常的处理 -- try-except-else-finally
    try语句处理逻辑：
        try语句执行，没有触发异常，则跳过except子句，try语句执行完毕
        触发异常时，则跳过try子句剩余部分。
        如果异常类型与except关键字后指定的异常相匹配，则执行except子句，try语句执行完毕
        没有匹配类型，则传递到外层try语句中。
        如果没有找到处理器，则是一个未处理的异常，执行将停止并输出错误信息

    except可接多个异常，但只有一个对应的处理器处理异常
        except (RuntimeError, TypeError, NameError):
            pass

        ***** except子句中的类匹配到的异常应该是该类本身的实例或者该类的派生类(反过来不行)
    
    BaseException是所有异常的基类，Exception是所有非致命异常的基类，非Exception子类的异常通常不被处理
    ***** 捕获异常的推荐做法：尽可能说明打算处理的异常类型，并允许任何意外的异常传播下去
        import sys

        try:
            f = open('myfile.txt')
            s = f.readline()
            i = int(s.strip())
        except OSError as err:
            print("OS error:", err)
        except ValueError:
            print("Could not convert data to an integer.")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise  # 抛出异常
    
    else子句
        必须放在所有except子句后面，适用于try子句没有引发异常但必须要执行的代码
    
    finally子句
        放在最后，无法try是否引发异常都会执行
        ***** 执行逻辑：
            如果执行 try 子句期间触发了某个异常，则某个 except 子句应处理该异常。如果该异常没有 except 子句处理，在 finally 子句执行后会被重新触发。
            except 或 else 子句执行期间也会触发异常。 同样，该异常会在 finally 子句执行之后被重新触发。
            如果 finally 子句中包含 break、continue 或 return 等语句，异常将不会被重新引发。
            如果执行 try 语句时遇到 break,、continue 或 return 语句，则 finally 子句在执行 break、continue 或 return 语句之前执行。
            如果 finally 子句中包含 return 语句，则返回值来自 finally 子句的某个 return 语句的返回值，而不是来自 try 子句的 return 语句的返回值。
    
3. 触发异常 -- raise，强制触发指定的异常
    raise + 异常类 or 异常实例 -- 必须是BaseException子类

4. 异常链
    异常发生在except子句中
        try:
            open("database.sqlite")
        except OSError:
            raise RuntimeError("unable to handle error")
        
        Traceback (most recent call last):
          File "<stdin>", line 2, in <module>
        FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'
        
        During handling of the above exception, another exception occurred:
        
        Traceback (most recent call last):
          File "<stdin>", line 4, in <module>
        RuntimeError: unable to handle error
        
    异常是某个异常的直接后果 -- 可选的from子句
        def func():
            raise ConnectionError
        
        try:
            func()
        except ConnectionError as exc:
            raise RuntimeError('Failed to open database') from exc
        
        Traceback (most recent call last):
          File "<stdin>", line 2, in <module>
          File "<stdin>", line 2, in func
        ConnectionError
        
        The above exception was the direct cause of the following exception:
        
        Traceback (most recent call last):
          File "<stdin>", line 4, in <module>
        RuntimeError: Failed to open database

5. 用户自定义异常
6. 异常组 -- ExceptionGroup，将多个异常放入列表中
    def f():
        excs = [OSError('error 1'), SystemError('error 2')]
        raise ExceptionGroup('there were problems', excs)

    f()
      + Exception Group Traceback (most recent call last):
      |   File "<stdin>", line 1, in <module>
      |   File "<stdin>", line 3, in f
      | ExceptionGroup: there were problems
      +-+---------------- 1 ----------------
        | OSError: error 1
        +---------------- 2 ----------------
        | SystemError: error 2
        +------------------------------------
    try:
        f()
    except Exception as e:
        print(f'caught {type(e)}: e')

    caught <class 'ExceptionGroup'>: e

7. 注解细化异常 -- add_note(note)
    try:
        raise TypeError('bad type')
    except Exception as e:
        e.add_note('Add some information')
        e.add_note('Add some more information')
        raise
    
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    TypeError: bad type
    Add some information
    Add some more information

"""


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


# B C D
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
