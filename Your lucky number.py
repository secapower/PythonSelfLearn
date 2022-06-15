from random import seed
from random import random

def numeroSuerte(nombre):
    numero =round(len(nombre) * random())
    print("Hola" + nombre + " tu numero de la suerte es" + str(numero))

numeroSuerte("Carlos")