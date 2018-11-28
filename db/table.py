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

    def select_all_row(self, attr_tuple):
        result = []
        for row in self:
            result.append(row.get(attr_tuple))
        return result

    def delete_row(self, key):
        for row in self:
            if row.key == key:
                self.remove(row)

    def pop_row(self, key):
        for i, row in enumerate(self):
            if row.key == key:
                return self.pop(i)

    def get_row(self, key):
        for i, row in enumerate(self):
            if row.key == key:
                return self[i]

    def load_file(self):
        print("load file")
        try:
            with open(self.file_name, 'rb') as f:
                item_list = pickle.load(f)
                self.extend(item_list)

        except FileNotFoundError:
            self.save_file()
        except Exception as e:
            print(e)

    def save_file(self):
        print("save file")
        with open(self.file_name, 'wb') as f:
            pickle.dump(self, f)

if __name__ == "__main__":
    from db.horse_info import Horse_Info
    horse_list = []
    horse_list.append(Horse_Info("Apple", "잘생기고 꼬리가 길다"))
    horse_list.append(Horse_Info("Bravo", "다리가 짧지만 빠르다"))
    horse_list.append(Horse_Info("Charlie", "당근을 좋아해서 뚱뚱하다"))
    horse_list.append(Horse_Info("Dragon", "내성적이라 수줍음이 많다"))
    horse_list.append(Horse_Info("Echo", "울음소리가 크다"))
    horse_list.append(Horse_Info("Fox", "달리는 모습이 아름답다"))
    horse_list.append(Horse_Info("Gang", "성격이 난폭하다"))
    horse_list.append(Horse_Info("Hide", "부상이 많아 경기 경험이 적다"))
    horse_list.append(Horse_Info("India", "외국에서 온 말로 비싸다"))
    horse_list.append(Horse_Info("Juliett", "암컷으로 매우 예쁘다"))
    horse_list.append(Horse_Info("Kate", "지능이 뛰어나다"))
    horse_list.append(Horse_Info("Lima", "아름다운 눈을 가졌다"))
    horse_list.append(Horse_Info("Mike", "체중 관리를 못해 뚱뚱하다"))
    horse_list.append(Horse_Info("November", "생일이 11월이다"))
    horse_list.append(Horse_Info("Oscar", "파란색을 좋아한다"))
    horse_list.append(Horse_Info("Papa", "나이가 많지만 경험이 많다"))
    horse_list.append(Horse_Info("Quebec", "캐나다에서 온 말로 프랑스어를 알아듣는다"))
    horse_list.append(Horse_Info("Romeo", "무식한게 용감하기만 하다"))
    horse_list.append(Horse_Info("Sierra", "비밀에 싸여있다"))
    horse_list.append(Horse_Info("Tango", "음악듣는 걸 좋아한다."))
    horse_list.append(Horse_Info("Uncle", "딴데보고 있으면 사라져있다."))
    horse_list.append(Horse_Info("Victory", "우승 경험이 많다"))
    horse_list.append(Horse_Info("Yankee", "주인이 부자다"))
    horse_list.append(Horse_Info("Zebra", "얼룩말이다"))

    t = Table("horse_info")
    t.extend(horse_list)
    t.file_name = "horse_info.dat"
    t.save_file()

    t2 = Table("horse_info")
    print(t2[22].name)

