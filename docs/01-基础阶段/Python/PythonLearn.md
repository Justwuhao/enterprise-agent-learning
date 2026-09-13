# Python 学习笔记
- python 装饰器(decorator)
## Python 装饰器 

### 装饰器的基本使用
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("before func")
        func(*args, **kwargs)
        print("after func")
    return wrapper
```
在函数前加`@decorator`即可使用装饰器
```python
@decorator
def func():
    print("func")
```
**原函数有返回值，装饰器也要返回值**
```python
def outer(func): 
    def res(*args,**kwargs):

        #执行原函数前触发
        print("before")

        value = func(*args, **kwargs)

        #执行原函数后触发
        print("after")

        return value #装饰器函数也必须要返回值
    return res

@outer
def SentWechat(body):
  print(body)
  return 100

if __name__ == "__main__":
  print(SentWechat("test message"))
```
