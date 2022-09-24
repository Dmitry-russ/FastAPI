from classies import Dragon, Chimera, Basilisk


#  наполнение классов из исходных данных
def data_load():
    data: dict = {
        "dragon": {
            0: {
                "name": "Горыныч",
                "weight": 240,
                "description": "просто дракон",
                "magic": "огонь",
                "wingspan": 143,
                "max_altitude": 2500,
            }
        },
        "chimera": {
            0: {
                "name": "Матильда",
                "weight": 100,
                "description": "обычная химера",
                "magic": "огонь",
                "max_speed": 135,
            }
        },
        "basilisk": {
            0: {
                "name": "Зубр",
                "weight": 112,
                "description": "среднеазиатский василиск",
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


#  для примеров запросов и ответов в redoc
post_examples = {
    "new": {
        "summary": "пример",
        "value": {
            "name": "Гора",
            "weight": 500,
            "description": "Замей горыныч",
            "magic": "Огонь",
            "wingspan": 100
        }
    },
}

patch_examples = {
    "change": {
        "summary": "пример",
        "value": {
            "description": "Замей горыныч",
            "magic": "Огонь"
        }
    },
}

get_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "get": {
                        "summary": "get_all",
                        "value": {
                            "dragon": {
                                0: {
                                    "name": "Горыныч",
                                    "weight": 240,
                                    "description": "описание",
                                    "magic": "огонь",
                                    "wingspan": 143,
                                    "max_altitude": 2500,
                                }
                            },
                            "chimera": {
                                0: {
                                    "name": "Матильда",
                                    "weight": 100,
                                    "description": "описание",
                                    "magic": "огонь",
                                    "max_speed": 135,
                                }
                            },
                            "basilisk": {
                                0: {
                                    "name": "Зубр",
                                    "weight": 112,
                                    "description": "описание",
                                    "magic": "яд",
                                    "strenght": 145,
                                }
                            },
                        }
                    }
                },
            }
        }
    }
}

get_class_response = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "get_class_response": {
                        "summary": "get_class_response",
                        "value": {
                            0: {
                                "name": "Зубр",
                                "weight": 112,
                                "description": "описание",
                                "magic": "яд",
                                "strenght": 145,
                            },
                            1: {
                                "name": "Матильда",
                                "weight": 100,
                                "description": "описание",
                                "magic": "огонь",
                                "max_speed": 135,
                            }

                        }
                    }}}}},
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "examples": {
                    "get_class_response": {
                        "summary": "get_class_response",
                        "value": {"error": "Class does not exist in data_base"}
                    }
                }}}}
}

get_id_response = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "get_id_response": {
                        "summary": "get_id_response",
                        "value": {
                            "name": "Зубр",
                            "weight": 112,
                            "description": "описание",
                            "magic": "яд",
                            "strenght": 145,
                        }
                    }
                }}}},
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "examples": {
                    "get_id_response": {
                        "summary": "get_id_response",
                        "value":
                            {"error": "id not found"}

                    }
                }}}}

}

del_response = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "del_response": {
                        "summary": "del_response",
                        "value": "Deleted: type {someone}, id {id}"
                    }
                }}}}}

post_response = {
    201: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "post_response": {
                        "summary": "post_response",
                        "value": {"created": {0: {
                            "name": "Гора",
                            "weight": 500,
                            "description": "Замей горыныч",
                            "magic": "Огонь",
                            "wingspan": 100
                        }}}
                    }
                }}}},
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "examples": {
                    "post_response": {
                        "summary": "post_response",
                        "value": {"error": "Class does not exist"}
                    }
                }}}},
    406: {
        "description": "Not Acceptable",
        "content": {
            "application/json": {
                "examples": {
                    "post_response": {
                        "summary": "post_response",
                        "value": {"error": "Not such attr. in this class. Check your data."}
                    }
                }}}},

}

patch_response = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "patch_response": {
                        "summary": "patch_response",
                        "value": {"changed": {0: {
                            "name": "Гора",
                            "weight": 500,
                            "description": "Замей горыныч",
                            "magic": "Огонь",
                            "wingspan": 100
                        }}}
                    }
                }}}},
    400: {
        "description": "Bad Request",
        "content": {
            "application/json": {
                "examples": {
                    "class problem": {
                        "summary": "class problem",
                        "value": {"error": "Class does not exist in data_base."}
                    },
                    "id problem": {
                        "summary": "id problem",
                        "value": {"error": "id not found."}
                    }
                },
            }
        }
    }}
