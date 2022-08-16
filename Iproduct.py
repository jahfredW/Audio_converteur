from abc import ABC, abstractmethod
from config import Config

class Iproduct(ABC):
    def __init__(self):
        self._type = ""
        self._caracteristiques = []

    def __str__(self):
        return self._type

    def analyser(self):
        print(f"Analyse du fichier {self._type} en cours")

    def convertir(self):
        print(f"convertion du fichier {self._type}")

    def exporter(self):
        print(f"exportation du fichier {self._type}")

        self.ajouter()

    def ajouter(self):
        c = Config()
        c.instances = self._type
        print(c)

