class Item():
    pay_rate = 0.9
    all=[]
    def __init__(self,name:str,quantity:int,price:int):

        #run validations to the recieved arguments
        assert quantity>0 , f"quantity {quantity} is not greater than zero"
        assert price>0, f"price {price} is not greater than zero"

        #assign to self object
        self.name=name
        self.quantity=quantity
        self.price=price
        #Actions to execute
        Item.all.append(self)
    
    def cal_total_price(self):
        return self.price*self.quantity
    def apply_discount(self):
        self.price=self.price*self.pay_rate
    def __repr__(self):
        return f"Item('{self.name}',{self.quantity},{self.price})"

# item1.name="Phone"
# item1.price=4500
# item1.quantity=3

#item2.pay_rate=0.5
# item2.name="Laptop"
# item2.price=50000
# item2.quantity=1

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))

# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item1.cal_total_price)
# #print(item1.cal_total_price(item1.price,item1.quantity)) 

# print(item2.name)
# print(item2.price)
# print(item2.quantity)
# print(item2.cal_total_price)
#print(item2.cal_total_price(item2.price,item2.quantity)) 
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(Item.__dict__)
# print(item1.__dict__)
# item1.apply_discount()
# print(item1.price)
# item2.apply_discount()
# print(item2.price)

item1=Item("phone",3,4500)
item2=Item("laptop",1,50000)
item3=Item("Cable",4,2000)
item4=Item("Mouse",7,400)
item5=Item("Keyboard",3,290) 

# for instance in Item.all:
#     print(instance.name)
print(Item.all)