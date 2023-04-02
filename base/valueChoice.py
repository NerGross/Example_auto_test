from random import choices, choice

import config


class ValueChoice:
    def params(self):
        param = {
            'VIN': choices(config.str_vin, k=17),
            'Регистрационный номер': (choices(config.str_rus, k=1)) + (choices(config.str_number, k=3)) + (
                choices(config.str_rus, k=2)) + (choices(config.str_number, k=3)),
            '№ шасси': choices(config.str_vin, k=17),
            '№ кузова': choices(config.str_vin, k=17)
        }
        key = choice(['VIN', 'Регистрационный номер', '№ шасси', '№ кузова'])
        return key, "".join(param[key])

#
# if __name__ == '__main__':
#     r = ValueChoice().params()
#     print(r[0],r[1])
