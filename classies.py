class base:
    def __init__(self, name, weight, description, magic, ):
        self.name = name
        self.weight = weight
        self.description = description
        self.magic = magic

    def patch_metod(self, data):
        self.name = (data["name"] if data["name"]
                     is not None else self.name)
        self.weight = (data["weight"] if data["weight"]
                       is not None else self.weight)
        self.description = (data["description"] if data["description"]
                            is not None else self.description)
        self.magic = (data["magic"] if data["magic"]
                      is not None else self.magic)


class Dragon(base):
    def __init__(self,
                 name: str,
                 weight: int,
                 description: str,
                 magic: str,
                 wingspan: int = None,
                 max_altitude: int = None
                 ) -> None:
        super().__init__(name, weight, description, magic, )
        self.wingspan = wingspan
        self.max_altitude = max_altitude

    def patch_metod(self, data):
        super().patch_metod(data)
        self.wingspan = (data["wingspan"] if data["wingspan"]
                         is not None else self.wingspan)
        self.max_altitude = (data["max_altitude"] if data["max_altitude"]
                             is not None else self.max_altitude)


class Chimera(base):
    def __init__(self,
                 name: str,
                 weight: int,
                 description: str,
                 magic: str,
                 max_speed: int = None,
                 ) -> None:
        super().__init__(name, weight, description, magic)
        self.max_speed = max_speed

    def patch_metod(self, data):
        super().patch_metod(data)
        self.max_speed = (data["max_speed"] if data["max_speed"]
                          is not None else self.max_speed)


class Basilisk(base):
    def __init__(self,
                 name: str,
                 weight: int,
                 description: str,
                 magic: str,
                 strenght: int = None,
                 ) -> None:
        super().__init__(name, weight, description, magic)
        self.strenght = strenght

    def patch_metod(self, data):
        super().patch_metod(data)
        self.strenght = (data["strenght"] if data["strenght"]
                         is not None else self.strenght)
