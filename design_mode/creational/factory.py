"""
简单工厂模式: 委托一个专门的函数或方法来创建实例
"""


class ChineseLocalizer:
    def __init__(self) -> None:
        self.translations = {"dog": "真的狗", "tiger": "你太虎了吧"}

    def localize(self, msg: str) -> str:
        return self.translations.get(msg, msg)


class EngilishLocalizer:
    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = "English") -> object:
    """Factory"""
    localizers = {
        "Chinese": ChineseLocalizer,
        "English": EngilishLocalizer
    }
    return localizers[language]()


def main():
    e, c = get_localizer(language='English'), get_localizer(language='Chinese')
    for msg in "dog cat tiger".split():
        print(e.localize(msg), c.localize(msg))


if __name__ == '__main__':
    main()
