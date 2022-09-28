#!/usr/bin/env python
# coding:utf-8

"""
@Time : 2022/9/28 20:27 
@Author : harvey
@File : c1.py 
@Software: PyCharm
@Desc: 
@Module
"""


class C1:
    age = 18

    def __new__(cls, *args, **kwargs):
        print("new", args)
        ins = super().__new__(cls, *args, **kwargs)
        print("instance age is", ins.age)
        return ins

    def __init__(self, name="jack"):
        print("init")
        self.name = name

    def __call__(self, *args, **kwargs):
        print("call")

    def echo(self):
        print("name is ", self.name)


if __name__ == '__main__':
    c1 = C1()
    print(vars(c1))
    print(dir(c1))
    c1.echo()
    c1("张三")  # 实例重载
    c1.echo()
