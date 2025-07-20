
class Phone:
    __current_voltage = 1

    def __keep_single_core(self):
        print("让cpu以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >=1:
            print("开启5g通话")
        else:
            self.__keep_single_core()
            print("电量不足")

phone = Phone()
phone.call_by_5g()

