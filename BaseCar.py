from CarExceptions import InvalidCarcassType, InvalidCompanyName, InvalidNewModelDataFormat
from CarExceptions import InvalidModelData, InvalidModelName

from typing import TypeVar, List, KeysView, Union

# test = {'Volkswagen AG': {'Polo 2017': 10},
#         'Toyota Motor': {'Camry': 25},
#         'Renault': {'Logan': 4},
#         'Nissan': {'Leaf': 55},
#         'Mitsubishi': {'Lancer': 65},
#         'Hyundai': {'Solaris': 2},
#         'Kia': {'Rio': 20},
#         'Ford Motor': {'Mustang': 10},
#         'Honda': {'Civic': 24},
#         'Suzuki': {'Vitara': 50},
#         'BMW': {'i3': 2},
#         'Mercedes-benz': {'E-class': 20},
#         'Tesla': {'Model 3': 200},
#         }


class CompanyDict:
    """Класс-хранилище.

    Attributes:
        _producers (dict[str, dict]): В качестве ключей содержит имена компаний, в соответствие которым ставится
        словарь моделей (ключи - имена моделей. Значения - количество моделей).
    """

    def __init__(self):
        self._producers = {'Volkswagen AG': {},
                           'Toyota Motor': {},
                           'Renault': {},
                           'Nissan': {},
                           'Mitsubishi': {},
                           'Hyundai': {},
                           'Kia': {},
                           'Ford Motor': {},
                           'Honda': {},
                           'Suzuki': {},
                           'BMW': {},
                           'Mercedes-benz': {},
                           'Tesla': {},
                           }

    def add_new_model(self, company_name: str, model_name: str, count: int) -> None:
        try:
            company_name_capitalize = company_name.capitalize()
            model_name_capitalize = model_name.capitalize()

            if company_name_capitalize in self._producers:
                if model_name_capitalize in self._producers[company_name_capitalize]:
                    self._producers[company_name_capitalize][model_name_capitalize] += count

                else:
                    self._producers[company_name_capitalize][model_name_capitalize] = count

            else:
                raise InvalidCompanyName

        except (ValueError, AttributeError):
            raise InvalidNewModelDataFormat('Company name and model name must be string, '
                                            'count must be integer.')

    def delete_model(self, company_name: str, model_name: str) -> Union[int, None]:
        try:
            company_name_capitalize = company_name.capitalize()
            model_name_capitalize = model_name.capitalize()

            if company_name_capitalize in self._producers:
                if model_name_capitalize in self._producers[company_name_capitalize]:
                    count_by_model = self._producers[company_name_capitalize][model_name_capitalize]

                    del self._producers[company_name_capitalize][model_name_capitalize]
                    return count_by_model
                else:
                    raise InvalidModelName

            else:
                raise InvalidCompanyName

        except (ValueError, AttributeError):
            raise InvalidNewModelDataFormat('Company name and model name must be string, '
                                            'count must be integer.')

    def is_model_in_dict(self, company_name: str, model_name: str) -> bool:
        """Этот метод мне не нравится. Но пока пусть будет."""
        try:
            if model_name in self._producers[company_name]:
                return True
        except KeyError:
            return False

    def is_company_in_dict(self, company_name: str) -> bool:
        """Этот метод мне не нравится. Но пока пусть будет."""
        try:
            if company_name in self._producers:
                return True
        except KeyError:
            return False

    def get_all_models_by_company(self, company_name: str) -> KeysView:
        """
        Принимает имя компании, проверяет есть ли соответствующая компания в словаре,
        возвращает список всех моделей соответствующей компании.

        :param company_name: имя компании.
        :return: список, в котором содержатся модели соответствующей компании.
        :raises InvalidCompanyName: если передано имя компании, которого нет в словаре.
        """
        try:
            return self._producers[company_name].keys()
        except KeyError:
            raise InvalidCompanyName

    def get_count_by_model(self, company_name, model_name: str) -> int:
        try:
            return self._producers[company_name][model_name]
        except KeyError:
            if company_name not in self._producers:
                raise InvalidCompanyName
            raise InvalidModelName


class BaseCar:

    companies = CompanyDict()

    __producer = TypeVar('__producer', bound='BaseCar.producer')  # Shit-style
    __carcass_type = TypeVar('__carcass_type', bound='BaseCar.carcass_type')  # Shit-style

    _carcass_types = ('Sedan', 'Hatchback', 'Station_wagon', 'Liftback',
                      'Coupe', 'Cabriolet', 'Roadster', 'Stretch',
                      'SUV', 'Crossover', 'Pickup', 'Van',
                      'Minivan')

    def __init__(self, producer, model_name, carcass_type, count, price):
        self.producer = producer
        self.model_name = model_name
        self.carcass_type = carcass_type
        self.count = count
        self.price = ...

        self.companies.add_new_model(producer, model_name, count)

    @property
    def producer(self) -> __producer:
        return self._producer

    @producer.setter
    def producer(self, value: __producer) -> None:
        if self.companies.is_company_in_dict(value):
            self._producer = value
        else:
            raise InvalidCompanyName

    @property
    def carcass_type(self) -> __carcass_type:
        return self._carcass_type

    @carcass_type.setter
    def carcass_type(self, value: _carcass_types) -> None:
        if value in self._carcass_types:
            self._carcass_type = value
        else:
            raise InvalidCarcassType

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value > 0:
            self._count = value
        else:
            raise InvalidNewModelDataFormat('The number of cars must be greater than 0')


class ICECar(BaseCar):
    pass


class ElectricCar(BaseCar):
    pass


if __name__ == '__main__':
    myCar = BaseCar('Tesla', 'Sedan')
    print(myCar.producer)
    myCar.producer = 'Volkswagen AG'
    print(myCar.producer)
    myCar.carcass_type = 'Coupe'
    print(myCar.carcass_type)

    cars = CompanyDict()
    cars.add_new_model('Tesla', 'Model 3', 10)
    print(cars.get_all_models_by_company('Tesla'))
    print(cars.get_count_by_model('Tesla', 'Model 3'))
    cars.delete_model('Tesla', 'Model 3')
