from random import choices, choice, randint
import config

car = [
    # [0-9]{4}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # [0-9]{4}[АВЕКМНОРСТУХ]{3}
    choices(config.str_number, k=4) + choices(config.str_rus, k=3),
    # [0-9]{3}[DT][0-9]{5,6}
    # choices(config.str_number, k=3) + choices(config.str_number, k=6),
    # [0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{3,4}
    choices(config.str_number, k=3) + choices(config.str_rus, k=2) + choices(config.str_number, k=4),
    # CD[0-9]{3}[DT][0-9]{2,3}
    # choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # К[АВЕКМНОРСТУХ]{2}[0-9]{5,6}
    #choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # [АВЕКМНОРСТУХ][0-9]{6,7}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # [АВЕКМНОРСТУХ][0-9]{4}[АВЕКМНОРСТУХ]{2}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # [АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # [АВЕКМНОРСТУХ]{2}[0-9]{4}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # [АВЕКМНОРСТУХ]{2}[0-9]{5,6}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # [АВЕКМНОРСТУХ]{2}[0-9]{6,7}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # [АВЕКМНОРСТУХ]{3}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # [АВЕКМНОРСТУХ]{3}[0-9]{4}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # С[АВЕКМНОРСТУХ]{2}[0-9]{5,6}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3),
    # Т[АВЕКМНОРСТУХ]{2}[0-9]{5,6}
    choices(config.str_number, k=4) + choices(config.str_rus, k=2) + choices(config.str_number, k=3)]

print("".join(car[randint(0, len(car) - 1)]))
