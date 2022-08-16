from mp3 import Mp3
from wave import Wave
from ConcreteFactory import ConcreteFactory
from Ifactory import IFactory
from config import Config


factory = ConcreteFactory()
product = factory.commander("mp3")
product2 = factory.commander("wave")
