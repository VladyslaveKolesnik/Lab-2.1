class RecipeScaler:
    def __init__(self, base_quantity: float, servings: int):
        self.base_quantity = base_quantity
        self.servings = servings

    @property
    def base_quantity(self) -> float:
        return self.__base_quantity

    @base_quantity.setter
    def base_quantity(self, value: float):
        if value <= 0:
            raise ValueError(" базова кількість має бути більшою за нуль")
        self.__base_quantity = value

    @property
    def servings(self) -> int:
        return self.__servings

    @servings.setter
    def servings(self, value: int):
        if value <= 0:
            raise ValueError(" кількість порцій має бути більшою за нуль")
        self.__servings = value

    def calculate_total_quantity(self) -> float:
        return self.__base_quantity * self.__servings

if __name__ == "__main__":
    try:
        user_base = float(input("Введіть базову кількість на 1 порцію: "))
        user_servings = int(input("Введіть кількість порцій: "))
        
        scaler = RecipeScaler(user_base, user_servings)
       
        print(scaler.calculate_total_quantity())
    except ValueError as error:
        print(error)