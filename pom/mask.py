import config
from random import randint
from random import choice, choices


class Mask:
    # with allure.step('test_1 00000000	^[0-9]{1,10}$'):
    # @staticmethod
    def test_1(self):
        return choices(config.str_number, k=randint(1, 10))

    # with allure.step('test_2 0000М55 ^[0-9]{4}[АВЕКМНОРСТУХ][0-9]{2,3}$'):
    # @staticmethod
    def test_2(self):
        return choices(config.str_number, k=4) + choices(config.str_rus) + choices(config.str_number, k=randint(2, 3))

    # with allure.step('test_3 0000ММ ^[0-9]{4}[АВЕКМНОРСТУХ]{2}$'):
    # @staticmethod
    def test_3(self):
        return choices(config.str_number, k=4) + choices(config.str_rus, k=2)

    # with allure.step('test_4 000М55 ^[0-9]{3}[АВЕКМНОРСТУХ][0-9]{2,3}$'):
    # @staticmethod
    def test_4(self):
        return choices(config.str_number, k=3) + choices(config.str_rus) + choices(config.str_number,
                                                                                   k=randint(2, 3))

    # with allure.step('test_5 222R00055 ^[0-9]{3}[DT][0-9]{5,6}$'):
    # @staticmethod
    def test_5(self):
        return choices(config.str_number, k=3) + choices(config.str_R) + choices(config.str_number, k=randint(5, 6))

    # with allure.step('test_6 222ММ055	^[0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{3,4}$'):
    # @staticmethod
    def test_6(self):
        return choices(config.str_number, k=3) + choices(config.str_rus, k=2) + choices(config.str_number,
                                                                                        k=randint(3, 4))

    # with allure.step('test_7 R2220055 ^[DT][0-9]{7,8}$'):
    # @staticmethod
    def test_7(self):
        return choices(config.str_R) + choices(config.str_number, k=randint(7, 8))

    # with allure.step('test_8 RR000R55	^CD[0-9]{3}[DT][0-9]{2,3}$'):
    # @staticmethod
    def test_8(self):
        return config.str_RR + choices(config.str_number, k=3) + choices(config.str_R) + choices(config.str_number,
                                                                                                 k=randint(2, 3))

    # with allure.step('test_9 К000ММ55 ^К[0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}$'):
    # @staticmethod
    def test_9(self):
        return config.str_K + choices(config.str_number, k=3) + choices(config.str_rus, k=2) + choices(
            config.str_number, k=randint(2, 3))

    # with allure.step('test_10 КММ00055 ^К[АВЕКМНОРСТУХ]{2}[0-9]{5,6}$'):
    # @staticmethod
    def test_10(self):
        return config.str_K + choices(config.str_rus, k=2) + choices(config.str_number, k=randint(5, 6))

    # with allure.step('test_11 М000055	^[АВЕКМНОРСТУХ][0-9]{6,7}$'):
    # @staticmethod
    def test_11(self):
        return choices(config.str_rus) + choices(config.str_number, k=randint(6, 7))

    # with allure.step('test1_12 М0000ММ ^[АВЕКМНОРСТУХ][0-9]{4}[АВЕКМНОРСТУХ]{2}$'):
    # @staticmethod
    def test_12(self):
        return choices(config.str_rus) + choices(config.str_number, k=4) + choices(config.str_rus, k=2)

    # with allure.step('test_13 М000ММ55 ^[АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}$'):
    # @staticmethod
    def test_13(self):
        return choices(config.str_rus) + choices(config.str_number, k=3) + choices(config.str_rus, k=2) + choices(
            config.str_number, k=randint(2, 3))

    # with allure.step('test_14 ММ0000 ^[АВЕКМНОРСТУХ]{2}[0-9]{4}$'):
    # @staticmethod
    def test_14(self):
        return choices(config.str_rus, k=2) + choices(config.str_number, k=4)

    # with allure.step('test_15 ММ000055 ^[АВЕКМНОРСТУХ]{2}[0-9]{6,7}$'):
    # @staticmethod
    def test_15(self):
        return choices(config.str_rus, k=2) + choices(config.str_number, k=randint(6, 7))

    # with allure.step('test_16 ММ00055	^[АВЕКМНОРСТУХ]{2}[0-9]{5,6}$'):
    # @staticmethod
    def test_16(self):
        return choices(config.str_rus, k=2) + choices(config.str_number, k=randint(5, 6))

    # with allure.step('test_17 ММ00ММ55 ^[АВЕКМНОРСТУХ]{2}[0-9]{2}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}$'):
    # @staticmethod
    def test_17(self):
        return choices(config.str_rus, k=2) + choices(config.str_number, k=2) + choices(config.str_rus, k=2) + choices(
            config.str_number, k=randint(2, 3))

    # with allure.step('test_18 ММ550000 ^[АВЕКМНОРСТУХ]{2}[0-9]{6,7}$'):
    # @staticmethod
    def test_18(self):
        return choices(config.str_rus, k=2) + choices(config.str_number, k=randint(6, 7))

    # with allure.step('test_19 МММ	^[АВЕКМНОРСТУХ]{3}$'):
    # @staticmethod
    def test_19(self):
        return choices(config.str_rus, k=3)

    # with allure.step('test_20 МММ0000	^[АВЕКМНОРСТУХ]{3}[0-9]{4}$'):
    # @staticmethod
    def test_20(self):
        return choices(config.str_rus, k=3) + choices(config.str_number, k=4)

    # with allure.step('test_21 СММ00055 ^С[АВЕКМНОРСТУХ]{2}[0-9]{5,6}$'):
    # @staticmethod
    def test_21(self):
        return config.str_C + choices(config.str_rus, k=2) + choices(config.str_number, k=randint(5, 6))

    # with allure.step('test_22 ТММ00055 ^Т[АВЕКМНОРСТУХ]{2}[0-9]{5,6}$'):
    # @staticmethod
    def test_22(self):
        return config.str_T + choices(config.str_rus, k=2) + choices(config.str_number, k=randint(5, 6))

    # with allure.step('test_23 ММ000М55 ^[АВЕКМНОРСТУХ]{2}[0-9]{3}[АВЕКМНОРСТУХ]{1}[0-9]{2,3}$'):
    # @staticmethod
    def test_23(self):
        return choices(config.str_rus, k=2) + choices(config.str_number, k=3) + choices(config.str_rus) + choices(
            config.str_number, k=randint(2, 3))
