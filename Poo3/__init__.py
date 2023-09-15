from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        return self.nombre == other.nombre

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return elemento in self.elementos

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.elementos = self.elementos.copy()
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nuevo_nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        elementos_interseccion = [elem for elem in conjunto1.elementos if elem in conjunto2.elementos]
        nuevo_conjunto = Conjunto(nuevo_nombre)
        nuevo_conjunto.elementos = elementos_interseccion
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ', '.join([elem.nombre for elem in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"

# Crear objetos Elemento
elem1 = Elemento("A")
elem2 = Elemento("B")
elem3 = Elemento("C")

# Crear conjuntos
conjunto1 = Conjunto("Conjunto1")
conjunto2 = Conjunto("Conjunto2")

# Agregar elementos a los conjuntos
conjunto1.agregar_elemento(elem1)
conjunto1.agregar_elemento(elem2)
conjunto2.agregar_elemento(elem2)
conjunto2.agregar_elemento(elem3)

# Realizar la unión de conjuntos
union = conjunto1 + conjunto2

# Realizar la intersección de conjuntos
interseccion = Conjunto.intersectar(conjunto1, conjunto2)

# Imprimir los conjuntos
print(conjunto1)
print(conjunto2)
print(union)
print(interseccion)
