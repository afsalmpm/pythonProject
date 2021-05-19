price =input('enter prices and press "f" to get the total ')
priceList=[]
#print(type (priceList))
while price != "f":
    price = int(price)
    #print(price)
    priceList.append(price)
    #print(priceList)
    price = input() #('enter prices and press "f" to get the total ')
print(f'Prices are {priceList}')
sum=0
for price in priceList:
    sum=sum+price
    #print(price)
print(f'\nTotal amount is {sum} rupees')
