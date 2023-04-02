from unittest import result

from base.valueChoice import ValueChoice


class VehicleManualFixture:
    s = None

    def test1(self):
        params = ValueChoice().params()
        print(type(params))
        print('test1', params[0], params[1])
        return params[1]

    def test2(self):
        test2 = self.test1()
        print('test2', test2)
        print(type(test2))


if __name__ == '__main__':
    test = VehicleManualFixture()
    #    result1 = test.test1()
    result2 = test.test2()
#    print('result1', result1)
#    print('result2', result2)
