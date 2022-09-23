from classies import Dragon, Chimera, Basilisk


#  наполнение классов из исходных данных
def data_load():
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
                "description": chimera_description,
                "magic": "огонь",
                "max_speed": 135,
            }
        },
        "basilisk": {
            0: {
                "name": "Зубр",
                "weight": 112,
                "description": basilisk_description,
                "magic": "яд",
                "strenght": 145,
            }
        },
    }

    classies_keys: dict = {
        "dragon": Dragon,
        "chimera": Chimera,
        "basilisk": Basilisk,
    }
    count: dict = {
        "dragon": 0,
        "chimera": 0,
        "basilisk": 0,
    }
    data_base: dict = {}
    for key, value in data.items():
        data_base[key] = {}
        for i_key, i_value in value.items():
            data_base[key][i_key] = classies_keys[key](**i_value)
            count[key] += 1
    return data_base, classies_keys
