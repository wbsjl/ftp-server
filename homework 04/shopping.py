goodlist = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

orderlist = []
total_price = 0

def go_shoppling():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buy(goodlist,orderlist)
        elif item == "2":
            pay(orderlist,goodlist,total_price)


def buy(goodlist, orderlist):

    for key, value in goodlist.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
    enter_code(goodlist, orderlist)



def enter_code(goodlist, orderlist):
    while True:
        cid = int(input("请输入商品编号："))
        if cid in goodlist:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    orderlist.append({"cid": cid, "count": count})
    print("添加到购物车。")


def pay(orderlist, goodlist, total_price):
    for item in orderlist:
        goods = goodlist[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (goods["name"], goods["price"], item["count"]))
        total_price += goods["price"] * item["count"]
    changes(orderlist, total_price)


def changes(orderlist, total_price):
    while True:
        Money = float(input("总价%d元，请输入金额：" % total_price))
        if Money >= total_price:
            print("购买成功，找回：%d元。" % (Money - total_price))
            orderlist.clear()
            break
        else:
            print("金额不足.")



go_shoppling()
