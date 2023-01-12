"""
Создать метакласс для паттерна Синглтон (см. конец вебинара)
"""


class MetaClassSingleton(type):
    instance = None

    def __new__(cls, name, age, dic):
        if cls.instance is None:
            cls.instance = type.__new__(cls, name, age, dic)
        else:
            return cls.instance
        return cls.instance

    def __init__(cls, name, age, dic):
        super(MetaClassSingleton, cls).__init__(name, age, dic)


class NameAge(metaclass=MetaClassSingleton):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print()
        print(f'Возраст объекта {self.name} - {self.age} лет')


obj = NameAge('Вася', 16)
obj.show()
obj_1 = NameAge('Валера', 18)
obj_1.show()
print()
print(obj is obj_1)
