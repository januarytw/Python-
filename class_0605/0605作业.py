# 1：创建一个名为 Restaurant 的类，其方法 init ()设置两个属性： restaurant_name 和 cooking_type。
# 创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，其中前者打印前述两项信息，
# 而后者打印一条消息， 指出餐馆正在营业。 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant():
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name=restaurant_name
        self.cooking_type=cooking_type
    def describe_restaurant(self):
        print("餐厅名字：%s 主营：%s"%(self.restaurant_name,self.cooking_type))

    def open_restaurant(self):
        print("餐厅正在营业！")

restaurant=Restaurant("蜀国演义","川菜")
restaurant.describe_restaurant()
restaurant.open_restaurant()



# 2:继承1 这个类，且添加函数：discount 打折扣用的 pay_money 支付餐费用 完成调用

class Restaurant_1(Restaurant):
    def discount(self,pay_money):
        print("您将享受8折优惠，优惠后价格：%s"%(int(pay_money)*0.8))

restaurant_1=Restaurant_1("海底捞","火锅")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.discount(100)



# 3:超继承1这个类的open_restaurant方法，多加一个优惠信息宣传。
class Restaurant_2(Restaurant):
    def open_restaurant(self):
        super(Restaurant_2,self).open_restaurant()
        print("餐厅正在营业，消费满100，可以享受8折优惠！")

restaurant_2=Restaurant_2("郭林家常菜","东北菜")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()