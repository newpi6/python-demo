class Single:
    _ins = None

    def __init__(self, name=None):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls._ins:
            return cls._ins
        cls._ins = super().__new__(cls, *args, **kwargs)
        return cls._ins

    def __str__(self):
        return f"<object: {self.name}>"


if __name__ == '__main__':
    s1 = Single()
    s2 = Single()
    print(id(s1), id(s2))
    print(s1)
    s1.name = "张三"
    print(s1)
    print(s2)
