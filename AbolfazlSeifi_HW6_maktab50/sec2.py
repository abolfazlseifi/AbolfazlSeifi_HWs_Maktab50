from sec1 import *
#################################
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
            if userid == i.get("userid"):
                username={"first_name":i.get("first_name"),"Last_name=":i.get("last_name")}
    temp = []
    for i in product_list:
        if i.get("type") == product_type:
            product_name = i.get("name")
            total_price= count*(i.get("price")+(i.get("price")*calculate_markup_percent(product_type,count))/100)
            for j in i.get("commission_groups"):
                for k in discount_list:
                    if j == k.get("group_name") and k.get("users")==userid:
                        if k.get("unit") == "percent":
                            temp.append((k.get("cost")/100)*total_price)
                        else:
                            temp.append(k.get("cost"))
    
    if len(temp) == 0:
        discont = 0
    else:
        discont = max(temp)
    total_with_commission=total_price-discont

    #print(product_name)
    #print(total_price)
    #print(total_with_commission)
    #print(discont)
    #print(username)
    return {"product_name":product_name,"total_price":total_price,
            "total_with_commission":total_with_commission,"discont":discont,"username":username}

print(calculate_product_price("1",10,1002))
print(calculate_product_price("1",15,1003))   
print(calculate_product_price("4",20,1005))
print(calculate_product_price("2",1))    