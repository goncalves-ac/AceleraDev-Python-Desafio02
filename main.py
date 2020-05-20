class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:

    def __init__(self, code, name, salary, departament):
        if (type(self) == Employee):
            raise TypeError('Employee não pode ser instanciado diretamente')
        self.code = code
        self.name = name
        self.salary = salary
        self.__departament = departament

    def get_departament(self):
        return self.__departament.name

    def set_department(self, departament):
        self.__departament.name = departament

    def calc_bonus(self):
        raise NotImplementedError("Implemente a função calc_bonus")

    def get_hours(self):
        return 8


class Manager(Employee):

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def put_sales(self, valor):
        self.__sales += valor

    def get_sales(self):
        return self.__sales

    def calc_bonus(self):
        return self.__sales * 0.15
