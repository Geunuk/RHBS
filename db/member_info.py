from db.table import Table

class Member_Info(Table):
    def __init__(self, member_id, pw, name, ssn, anum, email, pnum,  point=0):
        self.member_id = member_id
        self.password = pw
        self.name = name
        self.ssn = ssn
        self.account_number = anum
        self.email = email
        self.phone_number = pnum
        self.point = point
        self.key = (self.member_id,)

    def get(self, attr_tuple):
        result = []
        for attr in attr_tuple:
            if attr == "member_id":
                result.append(self.member_id)
            elif attr == "password":
                result.append(self.password)
            elif attr == "name":
                result.append(self.name)
            elif attr == "ssn":
                result.append(self.ssn)
            elif attr == "account_number":
                result.append(self.account_number)
            elif attr == "email":
                result.append(self.email)
            elif attr == "phone_number":
                result.append(self.phone_number)
            elif attr == "point":
                result.append(self.point)
            else:
                print("error in attr_tuple")
                return None

        return result