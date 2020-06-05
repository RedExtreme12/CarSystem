from CarExceptions import InvalidCarcassType, InvalidCompanyName, InvalidNewModelDataFormat
from CarExceptions import InvalidModelData

from typing import TypeVar


class CompanyDict:

    def __init__(self):
        """keys - Model, values - count."""
        self._producers = {'Volkswagen AG': {'Polo 2017': 10},
                           'Toyota Motor': {'Camry': 25},
                           'Renault': {'Logan': 4},
                           'Nissan': {'Leaf': 55},
                           'Mitsubishi': {'Lancer': 65},
                           'Hyundai': {'Solaris': 2},
                           'Kia': {'Rio': 20},
                           'Ford Motor': {'Mustang': 10},
                           'Honda': {'Civic': 24},
                           'Suzuki': {'Vitara': 50},
                           'BMW': {'i3': 2},
                           'Mercedes-benz': {'E-class': 20},
                           'Tesla': {'Model 3': 200},
                           }

    def add_new_model(self, company_name: str, model_name: str, count: int):
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

    def delete_model(self, company_name: str, model_name: str):
        try:
            company_name_capitalize = company_name.capitalize()
            model_name_capitalize = model_name.capitalize()

            if company_name_capitalize in self._producers:
                if model_name_capitalize in self._producers[company_name_capitalize]:
                    del self._producers[company_name_capitalize][model_name_capitalize]
                else:
                    raise InvalidModelData

            else:
                raise InvalidCompanyName

        except (ValueError, AttributeError):
            raise InvalidNewModelDataFormat('Company name and model name must be string, '
                                            'count must be integer.')


class BaseCar:
    __producer = TypeVar('__producer', bound='BaseCar.producer')
    __carcass_type = TypeVar('__carcass_type', bound='BaseCar.carcass_type')

    _carcass_types = ('Sedan', 'Hatchback', 'Station_wagon', 'Liftback',
                      'Coupe', 'Cabriolet', 'Roadster', 'Stretch',
                      'SUV', 'Crossover', 'Pickup', 'Van',
                      'Minivan')

    _producers = {'Volkswagen AG', 'Toyota Motor', 'Renault', 'Nissan',
                  'Mitsubishi', 'Hyundai', 'Kia', 'General Motors',
                  'Ford Motor', 'Honda', 'Suzuki', 'BMW', 'Daimler',
                  'Tesla'}

    def __init__(self, producer, carcass_type):
        self._producer = producer
        self._carcass_type = carcass_type

    @property
    def producer(self) -> __producer:
        return self._producer

    @producer.setter
    def producer(self, value: _carcass_types) -> None:
        if value in self._producers:
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


class ICECars(BaseCar):
    pass


class ElectricCars(BaseCar):
    pass


if __name__ == '__main__':
    myCar = BaseCar('sdasdasd', 'Sedan')
    print(myCar.producer)
    myCar.producer = 'Volkswagen AG'
    print(myCar.producer)
    myCar.carcass_type = 'Coupe'
    print(myCar.carcass_type)
