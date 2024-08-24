class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, hp):
        self.__color = color if color.lower() in self.__COLOR_VARIANTS else None
        self.owner = owner
        self.__model = model
        self.__engine_power = hp

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}', sep='\n')

    def set_color(self, new_color: str):
        if new_color.lower() not in self.__COLOR_VARIANTS:
            print(f'Нельзя сменить цвет на {new_color}')
            return
        self.__color = new_color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
