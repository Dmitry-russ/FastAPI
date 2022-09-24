class base:
    def __init__(self, name, weight, description, magic, ):
        self.name = name
        self.weight = weight
        self.description = description
        self.magic = magic


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
