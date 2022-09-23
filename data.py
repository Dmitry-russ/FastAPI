from classies import dragon, chimera, basilisk

chimera_description: str = (
    "в греческой мифологии[1] огнедышащее "
    "чудовище с головой и шеей льва, туловищем "
    "козы и хвостом в виде змеи; порождение Тифона и Ехидны[2]. "
    "В переносном смысле — необоснованная, несбыточная идея."
    )
basilisk_description: str = (
    "существо, толкуемое как ядовитая "
    "змея или как мифический чудовищный змей."
)
dragon_description: str = (
    "Драконы в восточных культурах обычно изображаются как "
    "бескрылые четвероногие существа с длинным змеевидным "
    "телом, обладающие определённым интеллектом."
)


data: dict = {
    "dragon": {
        0: {
            "name": "Горыныч",
            "weight": 240,
            "length": 95,
            "height": 75,
            "description": dragon_description,
            "magic": "огонь",
            "wingspan": 143,
            "max_altitude": 2500,
        }
    },
    "chimera": {
        0: {
            "name": "Матильда",
            "weight": 100,
            "length": 45,
            "height": 25,
            "description": chimera_description,
            "magic": "огонь",
            "max_speed": 135,
        }
    },
    "basilisk": {
        0: {
            "name": "Зубр",
            "weight": 112,
            "length": 146,
            "height": 10,
            "description": basilisk_description,
            "magic": "яд",
            "strenght": 145,
        }
    },
}


#  наполнение классов из исходных данных
def data_load(data):
    classies_keys: dict = {
        "dragon": dragon,
        "chimera": chimera,
        "basilisk": basilisk,
    }
    data_base: dict = {}
    for key, value in data.items():
        data_base[key] = {}
        for i_key, i_value in value.items():
            data_base[key][i_key] = classies_keys[key](**i_value)
    return data_base
