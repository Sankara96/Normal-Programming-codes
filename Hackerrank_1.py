
temp = (raw_input()).split()
no_items = temp[0]
k_item = temp[1]
price = raw_input().split()
price =[int(x) for x in price]
Charged_price = int(input())
dish_to_be_leftout = price[int(k_item)]
del price[int(k_item)]
sum_items = sum(price)
actual_price = sum_items/2
if actual_price == Charged_price:
    print "Bon Appetit"
elif actual_price<Charged_price:
    print "{0}".format(Charged_price-actual_price)

