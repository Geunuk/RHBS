class Game():
    def __init__(self, id, proceeding, result, horses, start_time, dividend_rate):
        self.__id = id
        self.__proceeding = proceeding
        self.__result = result
        self.__horses = horses
        self.__start_time = start_time
        self.__betting_info = None
        self.__dividend_rate = dividend_rate

    def calc_dividend_tate(self):
        ...

    def isvalid_proceeding(self):
        ...

    def add_betting_info(self, id, horse, point):
        ...

    def decide_result(self):
        ...

    def calc_dividend(self, horse, point):
        ...

    def show_game_result(self):
        ...
