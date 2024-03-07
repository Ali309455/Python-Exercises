from prettytable import PrettyTable
from functools import reduce
price_list = {'Maida':140, 'Wheat (Atta)' : 124, 'Suji': 170, 'Rice Superior':350 , 'White gram': 300, 'Black Gram': 280, 'Gram Pulse': 260, 'Mash': 430, 'Masoor': 200, 'Moong': 480, 'Dal Channa':260, 'Beson': 280,'Black Tea': 1800, 'Green tea': 1550, 'Sugar':130 , 'Curd': 180}
# store_items = [price_list.keys()]
store_items = list(price_list.keys())
# print(price_list['TapalDanedar'])
print(price_list[store_items[0]])

def showinfo():
    print(" Zahid General Store")
    for i,items in enumerate (store_items):
        i = i+1
        print(f'{i}.{items}')
def placeOrder(a):
   cart1 = price_list[store_items[a-1]]
   cart = store_items[a-1]
   b = float(input(f'How Much of {store_items[a-1]}:'))
   price = cart1 *b
   return cart, price,b
showinfo()
x =[]
y = []
z = []
print('ENTER THE NUMBER OF ITEM DISPLAYED AND WHEN THE BILL IS COMPLETED ENTER "0"')
def mysum(x, y):
  return x + y
def total_price():
    if y == []:
        return 0
    else:
        print('Im in Else statement')
        sum = reduce(mysum, y)
        sum =round(sum, 2)
        return sum
# for i in range (3):
while(True):
    e = int(input('Enter The items of the bill: '))
    # print(type(e))
    if e == 0:
        print('Agya')
        break
    else:
        x1,y1,z1 = placeOrder(e)
        x.append(x1)
        y.append(y1)
        z.append(z1)
        s1 = total_price()
        print(f'Your bill so far is: {s1}')

def receipt():
    table = PrettyTable()
    table.field_names = ['ITEMS','AMOUNT', 'PRICE']
    for T in range(len(x)):
        table.add_row([{x[T]},f'{z[T]}kg',f'{y[T]}Rs'])
        # table.add_row([x[T], f'{z[T]}kg', f'{y[T]}Rs'])

        print(T)
        # table.add_row([x[0],z[0],y[0]])
        # table.add_row([x[i-1],z[i-1],y[i-1]])
        # table.add_row([x[i],z[i],y[i]])
    table.add_row(['===== ','=====','====='])
    table.add_row(['TOTAL PRICE ','',s1])
    print(table)
# print(type(e))
print(x)
print(y)
print(z)
receipt()
# c = total_price()
# print(c)