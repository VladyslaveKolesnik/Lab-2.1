class SalaryCalculator:
    def __init__(self, gross_salary: float):
        self.gross_salary = gross_salary

    @property
    def gross_salary(self) -> float:
        return self.__gross_salary

    @gross_salary.setter
    def gross_salary(self, value: float):
        if value <= 0:
            raise ValueError(": зарплата має бути більшою за нуль")
        self.__gross_salary = value

    def calculate_net_salary(self) -> float:
        return self.__gross_salary * (1 - 0.195)

if __name__ == "__main__":
    try:
        user_input = float(input("Введіть зарплату до оподаткування: "))
        calculator = SalaryCalculator(user_input)
        print(calculator.calculate_net_salary())
    except ValueError as error:
        print(error)