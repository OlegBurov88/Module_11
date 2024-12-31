def introspection_info(obj):
    # Получение типа объекта
    obj_type = type(obj)

    # Получение атрибутов и методов объекта
    obj_attr = []
    obj_metod = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            obj_metod.append(attr)
        else:
            obj_attr.append(attr)

    # Получение модуля, к которому принадлежит объект
    obj_module = getattr(obj, '__module__', None)

    return {'Тип объекта': obj_type,
            'Атрибуты объекта': obj_attr,
            'Методы объекта': obj_metod,
            'Модуль': obj_module}


class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


number_info = introspection_info(42)
print(number_info)
print()
print(introspection_info('42'))
print()
print(introspection_info(introspection_info))
print()
print(introspection_info(House))
