import random

from db import table

class Game():
    def __init__(self, id, proceeding, result, horses, start_time, betting_info,dividend_rate):
        self.__id = id
        self.__proceeding = proceeding
        self.__result = result
        self.__horses = horses
        self.__start_time = start_time
        self.__betting_info = betting_info
        self.__dividend_rate = dividend_rate
        self.__login_account = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id


    @property
    def proceeding(self):
        return self.__proceeding

    @proceeding.setter
    def proceeding(self, proceeding):
        self.__proceeding = proceeding

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result):
        self.__result = result

    @property
    def horses(self):
        return self.__horses

    @horses.setter
    def horses(self, horses):
        self.__horses = horses

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def betting_info(self):
        return self.__betting_info

    @betting_info.setter
    def betting_info(self, betting_info):
        self.__betting_info = betting_info

    @property
    def dividend_rate(self):
        return self.__dividend_rate

    @dividend_rate.setter
    def dividend_rate(self, dividend_rate):
        self.__dividend_rate = dividend_rate

    @property
    def login_account(self):
        return self.__login_account

    @login_account.setter
    def login_account(self, login_account):
        self.__login_account = login_account

    def decide_result(self):
        self.__result = list(range(5))
        print(self.__result)
        random.shuffle(self.__result)
        print(self.__result)

    def calc_dividend_rate(self):
        print("calc_dividend_rate")
        sum = 0
        a = [0,0,0,0,0]
        for info in self.__betting_info:
            sum += int(info.bet_money)
            for row,horse in enumerate(self.__horses):
                if(horse.name == info.horse_name):
                    a[row] += int(info.bet_money)
        for i in range(5):
            if(a[i] != 0):
                self.__dividend_rate[i] = sum/a[i]
        #self.save_game_info()

    # 경기 종료 -> 멤버에게 넘겨줄 포인트 계산
    def calc_dividend(self):
        print("포인트를 되돌려주자")
        member_table = table.Table("member_info")
        print("1")
        idx = self.__result[0]
        print(self.__betting_info)
        for info in self.__betting_info:
            print("3")
            if(info.horse_name == self.__horses[idx].name):
                print("포인트 추가~~~")
                popped_member = member_table.pop_row((info.member_id,))

                popped_member.point += int(int(info.bet_money) * self.__dividend_rate[idx])
                member_table.append(popped_member)
                member_table.save_file()
                if(type(self.__login_account == 'Member.Member')):
                    self.__login_account.point += int(int(info.bet_money) * self.__dividend_rate[idx])

        print("4")