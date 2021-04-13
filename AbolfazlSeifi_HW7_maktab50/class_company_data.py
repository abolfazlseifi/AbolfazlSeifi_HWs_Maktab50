
##################################################
#######      Class of Company Data
##################################################


class Company_data:
    def __init__(self):
        pass


class User(Company_data):
    def __init__(self, userid: int, first_name: str, last_name: str):
        super(User, self).__init__()
        self.userid = userid
        self.first_name = first_name
        self.last_name = last_name


class Markup(Company_data):
    def __init__(self, product_type: str, lower_cost: int, upper_cost: int, unit: str, lower_count: int):
        super(Markup, self).__init__()
        self.product_type = product_type
        self.lower_cost = lower_cost
        self.upper_cost = upper_cost
        self.unit = unit
        self.lower_count = lower_count


class Discount(Company_data):
    def __init__(self, group_name: str, cost: int, unit: str, users: list):
        super(Discount, self).__init__()
        self.group_name = group_name
        self.cost = cost
        self.unit = unit
        self.users = users

    def validate_user(self,userid):
        for i in self.users:
            if i.userid == userid:
                return True


class Product(Company_data):
    def __init__(self, product_type: str, name: str, price: int, unit: str, commission_groups: list):
        super(Product, self).__init__()
        self.type = product_type
        self.name = name
        self.price = price
        self.unit = unit
        self.commission_groups = commission_groups


''' --------- Markup List -------------'''
m1 = Markup("1", 10, 20, "percent", 10)
m2 = Markup("2", 15, 20, "percent", 10)
m3 = Markup("3", 10, 15, "percent", 5)
m4 = Markup("4", 15, 20, "percent", 10)
markup_list = [m1, m2, m3, m4]
'''----------- User List ----------------'''
u1 = User(1001, "Mohsen", "Bayat")
u2 = User(1002, "Sobhan", "Taghadosi")
u3 = User(1003, "Javad", "Jafari")
u4 = User(1004, "Masoud", "Hosseini")
u5 = User(1005, "Hassan", "Zand")
u6 = User(1006, "Ali", "Ebadi")
user_list = [u1, u2, u3, u4, u5, u6]
'''---------  Discount Lis -----------'''
d1 = Discount("A", 5, "percent", [u1, u2, u3, u5])
d2 = Discount("B", 3, "Dollar", [u1, u3, u6])
d3 = Discount("C", 7, "percent", [u1, u2, u4])
discount_list = [d1, d2, d3]
'''------------- Product List ------------ '''
p1 = Product("1", "shirt", 30, "Dollar", [d1, d2])
p2 = Product("2", "pants", 50, "Dollar", [d1, d3])
p3 = Product("3", "shoes", 80, "Dollar", [d2])
p4 = Product("4", "hat", 20, "Dollar", [])
product_list = [p1, p2, p3, p4]


def calculate_markup_percent(a,b):
    for i in markup_list:
        if i.product_type == a:
            if b==1:
                return i.upper_cost
            elif b >= i.lower_count:
                return i.lower_cost
            else:
                s = i.lower_count-1
                t=i.upper_cost-i.lower_cost
                y=((t/s)*b)+i.lower_cost
                return y


def calculate_product_price(product_type,count,userid=1000):
    product_name=""
    total_price=0
    total_with_commission=0
    discont=0
    username=dict()
    if userid == 1000:
        username={"first_name":" ","Last_name=":" "}
    else:
        for i in user_list:
            if userid == i.userid:
                username={"first_name":i.first_name,"Last_name=":i.last_name}
    temp = []
    for i in product_list:
        if i.type == product_type:
            product_name = i.name
            total_price= count * (i.price + (i.price * calculate_markup_percent(product_type,count))/100)
            for j in i.commission_groups:
                for k in discount_list:
                    if j == k.group_name and k.users == userid:
                        if k.unit == "percent":
                            temp.append((k.cost / 100) * total_price)
                        else:
                            temp.append(k.cost)
    
    if len(temp) == 0:
        discont = 0
    else:
        discont = max(temp)
    total_with_commission = total_price - discont
    return {"product_name":product_name,"total_price":total_price,"total_with_commission":total_with_commission,"discont":discont,"username":username}

print(calculate_markup_percent("1", 2))
print(calculate_product_price("2", 10, 1001))
# print(calculate_product_price("1",10,1002))
# print(calculate_product_price("1",15,1003))   
# print(calculate_product_price("4",20,1005))
# print(calculate_product_price("2",1))
