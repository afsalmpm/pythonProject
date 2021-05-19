import Stock_functions
import Stock_to_Xcel_functions


class Stock:
    def __init__(self, stock_name, date):
        self.stock_name = stock_name
        self.date = date

    def delivery_buy(self):
        delivery_buy_list = Stock_functions.equity_delivery_buy_entry(self.stock_name, self.date)
        print("Processing.....")
        Stock_to_Xcel_functions.to_add_to_common_and_to_add_jasi(self.stock_name, delivery_buy_list, "delivery buy")

    def delivery_sell(self):
        delivery_sell_list = Stock_functions.equity_delivery_sell_entry(self.stock_name, self.date)
        print("Processing.....")
        Stock_to_Xcel_functions.to_add_to_common_and_to_add_jasi(self.stock_name, delivery_sell_list, "delivery sell")

    def intra_day(self):
        intra_day_list = Stock_functions.equity_intraday_entry(self.stock_name, self.date)
        print("Processing.....")
        Stock_to_Xcel_functions.to_add_to_common_and_to_add_jasi(self.stock_name, intra_day_list, "intra day")


# ***********The program starts here ************** #
transaction_date = Stock_functions.date_entry("Transaction date")
while True:
    equity_name = (input("Enter the Symbol: ")).upper()
    if equity_name != '':
        equity_name = Stock(equity_name, transaction_date)
    else:
        print('Invalid "Symbol" Entry... Enter again!!!')
        continue
    while True:
        choice = input("""
Select your choice
Delivery trade Buy  : 1
Delivery trade Sell : 2
Intraday trade      : 3
>>""")
        if choice == "1":
            equity_name.delivery_buy()
            break
        elif choice == "2":
            equity_name.delivery_sell()
            break
        elif choice == "3":
            equity_name.intra_day()
            break
        else:
            print("Invalid Choice")
    xit = input("Completed successfully \n\nTo add another Symbol press Space+Enter")
    if xit == " ":
        continue
    else:
        break
