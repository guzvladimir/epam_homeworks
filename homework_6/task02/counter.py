"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    cls.counter = 0

    def __new__(cls):
        instance = super(cls, cls).__new__(cls)
        cls.counter += 1
        return instance

    @classmethod
    def get_created_instances(cls):
        return cls.counter

    @classmethod
    def reset_instances_counter(cls):  # self = None или ещё как-то
        last_value = cls.counter
        cls.counter = 0
        return last_value

    setattr(cls, "__new__", __new__)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)
    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
