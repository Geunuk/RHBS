class Game_Manager:
    def __init__(self):
        self.__game_list = None
        self.__horse_list = None

    @property
    def game_list(self):
        return self.__game_list

    @game_list.setter
    def game_list(self, game_list):
        self.__game_list = game_list

    @property
    def horse_list(self):
        return self.__horse_list

    @horse_list.setter
    def horse_list(self, horse_list):
        self.__horse_list = horse_list

    def check_game_finish(self):
        ...

    def init_game(self):
        ...

    def show_game_status(self):
        ...

    def show_betting_result(self):
        ...

    def read_game_file(self):
        ...

    def save_game_file(self):
        ...

    def read_betting_file(self):
        ...

    def save_betting_file(self):
        ...

    def read_horse_file(self):
        ...