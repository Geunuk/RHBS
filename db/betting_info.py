from db.table import Table

class Betting_Info(Table):
    def __init__(self, member_id, game_id, horse_name, bet_money):
        self.member_id = member_id
        self.game_id = game_id
        self.hose_name = horse_name
        self.bet_money = bet_money
        self.key = (self.member_id,self.game_id)

    def get(self, attr_tuple):
        result = []
        for attr in attr_tuple:
            if attr == "member_id":
                result.append(self.member_id)
            elif attr == "game_id":
                result.append(self.game_id)
            elif attr == "horse_name":
                result.append("horse_name")
            elif attr == "bet_money":
                result.append(self.bet_money)
            else:
                print("error in attr_tuple")
                return None

        return result