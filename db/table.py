import pickle


class Table(list):
    def __init__(self, name):
        self.name = name
        self.file_name = "db/" + name + ".dat"
        self.load_file()

    def select_row(self, key, attr_tuple):
        for row in self:
            if row.key == key:
                return row.get(attr_tuple)
        else:
            return False

    def delete_row(self, key):
        for row in self:
            if row.key == key:
                self.remove(row)

    def pop_row(self, key):
        for i, row in enumerate(self):
            if row.key == key:
                return self.pop(i)

    def load_file(self):
        try:
            with open(self.file_name, 'rb') as f:
                item_list = pickle.load(f)
                self.extend(item_list)

        except:
            self.save_file()


    def save_file(self):
        print("save file")
        with open(self.file_name, 'wb') as f:
            pickle.dump(self, f)

if __name__ == "__main__":
    from db.horse_info import Horse_Info
    horse1 = Horse_Info("Apple", "잘생김")
    horse2 = Horse_Info("Bravo", "다리김")
    horse3 = Horse_Info("Charlie", "당근좋아함")
    horse_list = [horse1, horse2, horse3]
    t = Table("horse_info")
    t.extend(horse_list)
    t.save_file("horse_info.dat")
    t2 = Table("horse_info")
    t2.load_file("horse_info.dat")

    print(t2.select_row(("Apple",), ("name", "feature", "rating")))
    t2.delete_row(("Apple",))
    print(t2.select_row(("Apple",), ("name", "feature", "rating")))