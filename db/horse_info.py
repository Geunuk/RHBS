from db.table import Table


class Horse_Info(Table):
    def __init__(self, name, feature, rating=1500):
        self.name = name
        self.feature = feature
        self.rating = rating
        self.key = (self.name,)

    def get(self, attr_tuple):
        result = []
        for attr in attr_tuple:
            if attr == "name":
                result.append(self.name)
            elif attr == "feature":
                result.append(self.feature)
            elif attr == "rating":
                result.append("rating")
        return result