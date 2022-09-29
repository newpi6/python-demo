"""
具备__iter__、__next__方法的对象都是迭代器
"""

"""
for循环过程：
1. 调用对象的__iter__方法，生成iterator对象
2. 调用对象的__next__方法
3. 直到抛出StopIteration异常(for语句会捕捉该异常)，循环终止
"""


class MyRange:
    def __init__(self, limit=100):
        self.limit = limit
        self.number = 0

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        self.number += 1
        if self.number > self.limit:
            raise StopIteration
        return self.number


def loop1():
    for i in MyRange():
        print(i)


def loop2():
    i = MyRange(100)
    for x in i:
        print(x)
    # print(i.__next__())
    # print(i.__next__())
    # print(i.__next__())


def loop3():
    i = MyRange(100)
    myIter = iter(i)  # 等价于 myIter = i.__iter__()
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))  # 循环到3
    for y in myIter:  # 从0循环，取决于__iter__方法中是否初始化起始值
        print(y)


if __name__ == '__main__':
    loop3()
