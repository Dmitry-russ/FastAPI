class base:
    def __init__(self, name, weight, length, height, description, magic,):
        self.name = name
        self.weight = weight
        self.length = length
        self.height = height
        self.description = description
        self.magic = magic


class dragon(base):
    def __init__(self,
                 name: str,
                 weight: int,
                 length: int,
                 height: int,
                 description: str,
                 magic: str,
                 wingspan: int,
                 max_altitude: int
                 ) -> None:
        super().__init__(name, weight, length, height, description, magic)
        self.wingspan = wingspan
        self.max_altitude = max_altitude


class chimera(base):
    def __init__(self,
                 name: str,
                 weight: int,
                 length: int,
                 height: int,
                 description: str,
                 magic: str,
                 max_speed: int,
                 ) -> None:
        super().__init__(name, weight, length, height, description, magic)
        self.max_speed = max_speed


class basilisk(base):
    def __init__(self,
                 name: str,
                 weight: int,
                 length: int,
                 height: int,
                 description: str,
                 magic: str,
                 strenght: int,
                 ) -> None:
        super().__init__(name, weight, length, height, description, magic)
        self.strenght = strenght
