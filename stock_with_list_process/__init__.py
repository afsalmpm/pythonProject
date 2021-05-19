import Stock_functions
import read_process_write_list_to_excel
import To_email_backup
import Resetting_the_excel_for_next_month


class Stock:
    def __init__(self, stock_name, date):
        self.stock_name = stock_name
        self.date = date

    def delivery_buy(self):
        delivery_buy_list = Stock_functions.equity_delivery_buy_entry(self.stock_name, self.date)
        print("Processing.....")
        read_process_write_list_to_excel.to_add_to_common_and_to_add_jasi(delivery_buy_list, "delivery buy")

    def delivery_sell(self):
        delivery_sell_list = Stock_functions.equity_delivery_sell_entry(self.stock_name, self.date)
        print("Processing.....")
        read_process_write_list_to_excel.to_add_to_common_and_to_add_jasi(delivery_sell_list, "delivery sell")

    def intra_day(self):
        intra_day_list = Stock_functions.equity_intraday_entry(self.stock_name, self.date)
        print("Processing.....")
        read_process_write_list_to_excel.to_add_to_common_and_to_add_jasi(intra_day_list, "intra day")


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
         Delivery trade Sell  : 2
              Intraday trade  : 3
      Email files for backup  : 4
Abort operation or reset file : 5
>>>>>>>>>>>>>>>>>>>> :""")
        if choice == "1":
            equity_name.delivery_buy()
            break
        elif choice == "2":
            equity_name.delivery_sell()
            break
        elif choice == "3":
            equity_name.intra_day()
            break
        elif choice == "4":
            print("Processing.....")
            To_email_backup.email_backup(transaction_date)
            break
        elif choice == "5":
            rest = input('\nDo you want to reset the files for next month? press "y":')
            if rest == "y":
                Resetting_the_excel_for_next_month.to_reset_excel_file()
                break
            else:
                break
        else:
            print("Invalid Choice")
    xit = input("Finished the process!! \n\nTo do more: press Space+Enter")
    if xit == " ":
        continue
    else:
        break
