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

    def calc_dividend_rate(self):
        print("calc_dividend_rate")
        sum = 0
        a = [0,0,0,0,0]
        for info in self.__betting_info:
            #print(info.bet_money)
            sum += int(info.bet_money)
            for row,horse in enumerate(self.__horses):
                #print(horse.name)
                if(horse.name == info.horse_name):
                    a[row] += int(info.bet_money)
        for i in range(5):
            if(a[i] != 0):
                self.__dividend_rate[i] = sum/a[i]
                #print(self.__dividend_rate[i])
        self.save_game_info()

    def isvalid_proceeding(self):
        ...

    def add_betting_info(self, id, horse, point):
        ...

    def decide_result(self):
        ...

#   경기 종료 -> 멤버에게 넘겨줄 포인트 계산
    def calc_dividend(self, horse, point):
        ...

    def show_game_result(self):
        ...

    def save_game_info(self):
        game_table = table.Table("game_info")
        popped_game = game_table.pop_row((self.__id,))

        popped_game.dividend_rate = self.__dividend_rate
        game_table.append(popped_game)
        game_table.save_file()