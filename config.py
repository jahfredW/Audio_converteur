from singleton import Singleton

class Config(metaclass=Singleton):
    def __init__(self):
        self._config = {}
        self._instances = []
        self.init()

    def __str__(self):
        return str(self._instances)

    @property
    def instances(self):
        return self._instances

    @instances.setter
    def instances(self, value):
        self._instances.append(value)



    def init(self):
        self._config = {
            'user': 'fred',
            'id': 1234,
            'license': 'trial',
            'instances': self._instances
        }


