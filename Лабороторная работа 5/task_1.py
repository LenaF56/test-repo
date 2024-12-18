# TODO Написать 3 класса с документацией и аннотацией типов

class HolidayDecoration:
    def __init__(self, color: str, material: str):
        """
        Создание и подготовка к работе объекта "Новогоднее украшение"

        :param color: Цвет украшения
        :param material: Материал украшения

        Примеры:
        >>> decoration = HolidayDecoration("красный", "стекло")
        >>> decoration.color
        'красный'
        """
        if not isinstance(color, str):
            raise TypeError("Цвет украшения должен быть строкой")
        if not isinstance(material, str):
            raise TypeError("Материал украшения должен быть строкой")
        self.color = color
        self.material = material

    def display(self) -> str:
        """
        Отображение информации об украшении.

        :return: Описание украшения

        Примеры:
        >>> decoration = HolidayDecoration("красный", "стекло")
        >>> decoration.display()
        'Украшение: цвет - красный, материал - стекло'
        """
        return f'Украшение: цвет - {self.color}, материал - {self.material}'

    def replace(self, new_color: str) -> None:
        """
        Изменение цвета украшения.

        :param new_color: Новый цвет украшения

        Примеры:
        >>> decoration = HolidayDecoration("красный", "стекло")
        >>> decoration.replace("зеленый")
        >>> decoration.color
        'зеленый'
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет должен быть строкой")
        self.color = new_color


class Gift:
    def __init__(self, recipient: str, content: str):
        """
        Создание и подготовка к работе объекта "Подарок"

        :param recipient: Получатель подарка
        :param content: Содержимое подарка

        Примеры:
        >>> gift = Gift("Саша", "Кубик Рубик")
        >>> gift.recipient
        'Саша'
        """
        if not isinstance(recipient, str):
            raise TypeError("Имя получателя должно быть строкой")
        if not isinstance(content, str):
            raise TypeError("Содержимое подарка должно быть строкой")
        self.recipient = recipient
        self.content = content

    def unwrap(self) -> str:
        """
        Разворачивание подарка.

        :return: Описание процесса разворачивания подарка

        Примеры:
        >>> gift = Gift("Саша", "Кубик Рубик")
        >>> gift.unwrap()
        'Саша раскрыл подарок: Кубик Рубика'
        """
        return f'{self.recipient} раскрыл подарок: {self.content}'

    def change_recipient(self, new_recipient: str) -> None:
        """
        Изменение получателя подарка.

        :param new_recipient: Новый получатель

        Примеры:
        >>> gift = Gift("Саша", "Кубик Рубик")
        >>> gift.change_recipient("Маша")
        >>> gift.recipient
        'Маша'
        """
        if not isinstance(new_recipient, str):
            raise TypeError("Имя нового получателя должно быть строкой")
        self.recipient = new_recipient


class ChristmasTree:
    def __init__(self, height: int):
        """
        Создание и подготовка к работе объекта "Новогодняя елка"

        :param height: Высота елки

        Примеры:
        >>> tree = ChristmasTree(5)
        >>> tree.height
        5
        """
        if not isinstance(height, int):
            raise TypeError("Высота елки должна быть целым числом")
        if height <= 0:
            raise ValueError("Высота елки должна быть положительным числом")
        self.height = height
        self.decorations = []

    def decorate(self, decoration: HolidayDecoration) -> None:
        """
        Добавление украшения на елку.

        :param decoration: Украшение

        Примеры:
        >>> tree = ChristmasTree(5)
        >>> _decoration = HolidayDecoration("красный", "стекло")
        >>> tree.decorate(decoration)
        >>> len(tree.decorations)
        1
        """
        self.decorations.append(decoration)

    def show_decorations(self) -> str:
        """
        Отображение всех украшений на елке.

        :return: Описание всех украшений

        Примеры:
        >>> tree = ChristmasTree(5)
        >>> decoration1 = HolidayDecoration("красный", "стекло")
        >>> decoration2 = HolidayDecoration("золотой", "пластик")
        >>> tree.decorate(decoration1)
        >>> tree.decorate(decoration2)
        >>> tree.show_decorations()
        'Украшение: цвет - красный, материал - стекло\n Украшение: цвет - золотой, материал - пластик'
        """
        return '\n'.join(deco.display() for deco in self.decorations) if self.decorations else "Нет украшений"


if __name__ == "__main__":
 # TODO работоспособность экземпляров класса проверить с помощью doctest
 pass
