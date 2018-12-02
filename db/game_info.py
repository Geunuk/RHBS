from db.table import Table


class Game_Info(Table):
    def __init__(self, game_id, start_time, result, horses, dividend_rate, proceeding):
        self.game_id = game_id
        self.start_time = start_time
        self.result = result
        self.horses = horses
        self.dividend_rate = dividend_rate
        self.proceeding = proceeding
        self.key = (self.game_id, )

    def get(self, attr_tuple):
        result = []
        for attr in attr_tuple:
            if attr == "game_id":
                result.append(self.game_id)
            elif attr == "start_time":
                result.append(self.start_time)
            elif attr == "result":
                result.append("result")
            elif attr == "horses":
                result.append(self.horses)
            elif attr == "dividend_rate":
                result.append(self.dividend_rate)
            elif attr == "proceeding":
                result.append(self.proceeding)
            else:
                print("error in attr_tuple")
                return None

        return result