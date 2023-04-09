from random import choices, choice
import config


class ValueChoice:
    @staticmethod
    def params():
        param = {
            'VIN': choices(config.str_vin, k=17),
            'Регистрационный номер': (choices(config.str_rus, k=1)) + (choices(config.str_number, k=3)) + (
                choices(config.str_rus, k=2)) + (choices(config.str_number, k=3)),
            '№ шасси': choices(config.str_vin, k=17),
            '№ кузова': choices(config.str_vin, k=17)
        }
        key = choice(['VIN', 'Регистрационный номер', '№ шасси', '№ кузова'])
        return key, "".join(param[key])

    @staticmethod
    def vehicle_doc():
        doc_vehicle = choices(config.str_number, k=2) + choices(config.str_rus, k=2)
        doc_vehicle_number = choices(config.str_number, k=6)
        return [doc_vehicle, doc_vehicle_number]

    @staticmethod
    def vehicle_doc_to():
        vehicle_doc_to_number = choices(config.str_number, k=21)
        return vehicle_doc_to_number

