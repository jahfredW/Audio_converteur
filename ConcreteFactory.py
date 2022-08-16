from Ifactory import IFactory
from mp3 import Mp3
from wave import Wave

class ConcreteFactory(IFactory):
    def creer(self, type_format):
        if type_format == "mp3":
            return Mp3()
        elif type_format == 'wave':
            return Wave()
        else:
            raise NotImplementedError("Le format n'a pas été implémenté")


