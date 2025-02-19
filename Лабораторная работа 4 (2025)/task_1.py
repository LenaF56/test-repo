if __name__ == "__main__":
    # Write your solution here
    pass

class Animal:
    """Базовый класс для животных."""

    def __init__(self, name: str, age: int):
        """
        Инициализация животного.

        :param name: Имя животного.
        :param age: Возраст животного в годах.
        """
        self._name = name  # Имя животного (непубличный атрибут)
        self._age = age  # Возраст животного (непубличный атрибут)

    @property
    def name(self) -> str:
        """Возвращает имя животного."""
        return self._name

    @property
    def age(self) -> int:
        """Возвращает возраст животного."""
        return self._age

    def speak(self) -> str:
        """Издает звук животного. Метод должен быть переопределен в дочерних классах."""
        raise NotImplementedError("Метод speak() должен быть переопределен в дочернем классе.")

    def __str__(self) -> str:
        """Возвращает строковое представление животного."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age})"

    def __repr__(self) -> str:
        """Возвращает представление объекта для отладки."""
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age})"


class Dog(Animal):
    """Класс для собак, наследуется от Animal."""

    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация собаки.

        :param name: Имя собаки.
        :param age: Возраст собаки в годах.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)  # Вызов конструктора базового класса
        self._breed = breed  # Порода собаки (непубличный атрибут)

    @property
    def breed(self) -> str:
        """Возвращает породу собаки."""
        return self._breed

    def speak(self) -> str:
        """Издает звук собаки."""
        return "Гав!"

    def __str__(self) -> str:
        """Возвращает строковое представление собаки."""
        return f"Собака {self.name}, возраст {self.age}, порода {self.breed}"


class Cat(Animal):
    """Класс для кошек, наследуется от Animal."""

    def __init__(self, name: str, age: int, color: str):
        """
        Инициализация кошки.

        :param name: Имя кошки.
        :param age: Возраст кошки в годах.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)  # Вызов конструктора базового класса
        self._color = color  # Цвет кошки (непубличный атрибут)

    @property
    def color(self) -> str:
        """Возвращает цвет кошки."""
        return self._color

    def speak(self) -> str:
        """Издает звук кошки."""
        return "Мяу!"

    def __str__(self) -> str:
        """Возвращает строковое представление кошки."""
        return f"Кошка {self.name}, возраст {self.age}, цвет {self.color}"


if __name__ == "__main__":
    # Примеры использования
    dog = Dog("Шарик", 3, "Лабрадор")
    cat = Cat("Мурка", 2, "Черный")

    print(dog)  # Вывод информации о собаке
    print(dog.speak())  # Вывод звука собаки

    print(cat)  # Вывод информации о кошке
    print(cat.speak())  # Вывод звука кошки
