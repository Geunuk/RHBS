class Horse():
    def __init__(self, name, feature, rating):
        self.__name = name
        self.__feature = feature
        self.__rating = rating

    @property
    def name(self):
        return self.__name

    @property
    def feature(self):
        return self.__feature

    def calc_horse_rating(self):
        ...

if __name__ == "__main__":
    a = Horse("a", "123", 2000)
    c = Horse("b", "123", 2000)
    d = Horse("c", "123", 2000)
