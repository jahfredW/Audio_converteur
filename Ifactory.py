from abc import ABC, abstractmethod

class IFactory(ABC):
    def commander(self, type_format):
        product = self.creer(type_format)
        product.analyser()
        product.convertir()
        product.exporter()
        return product

    @abstractmethod
    def creer(self, type_format):
        pass