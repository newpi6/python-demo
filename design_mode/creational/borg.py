from typing import Dict

"""
共享实例状态
"""


class Borg:
    _shared_state: Dict[str, str] = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class YourBorg(Borg):
    def __init__(self, state: str = None):
        super().__init__()
        if state:
            self.state = state
        else:
            if not hasattr(self, "state"):
                self.state = "Init"

    def __str__(self):
        return f"<object: {self.state}>"


def main():
    obj1 = YourBorg()
    obj2 = YourBorg()
    print(id(obj1), id(obj2))
    print(obj2.__dict__)
    obj1.state = "sleep"
    print(obj1)
    print(obj2)
    print(obj2.__dict__)
    obj3 = YourBorg()
    print(obj3)

if __name__ == '__main__':
    main()
