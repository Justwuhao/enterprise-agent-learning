'''
def outer(func): #定义一个装饰器函数outer
    def res(*args,**kwargs):

        #执行原函数前触发
        print("before")

        func(*args, **kwargs)

        #执行原函数后触发
        print("after")

    return res

@outer
def SentWechat(body):
  print(body)

if __name__ == "__main__":
  SentWechat("test message")

'''


def outer(func): #返回值问题
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
