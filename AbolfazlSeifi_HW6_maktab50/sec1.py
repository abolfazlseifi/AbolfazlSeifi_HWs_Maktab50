from company_data import *
#############################################################
def calculate_markup_percent(a,b):
    for i in markup_list:
        if i.get("product_type") == a:
            if b==1:
                return i.get("upper_cost")
            elif b >= i.get("lower_count"):
                return i.get("lower_cost")
            else:
                s = i.get("lower_count")-1
                t=i.get("upper_cost")-i.get("lower_cost")
                y=((t/s)*b)+i.get("lower_cost")
                return y

print(calculate_markup_percent("1",5))
print(calculate_markup_percent("2",1))
print(calculate_markup_percent("3",20))
