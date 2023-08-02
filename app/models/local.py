import json

class Destino:
    def __init__(self, id_local, nombre, tipo_cosina, ingredientes, precio_min, precio_max, popularidad, disponibilidad, id_ubicacion, imagen,):
        self.id_local = id_local
        self.nombre = nombre
        self.tipo_cosina = tipo_cosina
        self.ingredientes = ingredientes
        self.precio_min = precio_min
        self.precio_max = precio_max
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen


    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)

    @staticmethod
    def cargar_locales(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
        return [Destino.de_json(json.dumps(dato)) for dato in datos]