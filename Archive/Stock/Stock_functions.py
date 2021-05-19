def date_entry(date_to_be_entered):  # date entry function
    from datetime import date
    today_confirmation = input('\nPress "n" if the Date of transaction is not today: ')
    if today_confirmation != "n":
        today = date.today()
        x = str(today)
        [year, month, day] = x.split("-")
        date = f'{day}/{month}/{year}'
        date_to_be_entered = date
    else:
        while True:
            # While loop should continue "loop exit value" is equal to "value error"
            try:
                date_format = input(f'Enter {date_to_be_entered} in "dd/mm/yyyy" format: ')
                [day, month, year] = date_format.split("/")
                day_int = int(day)
                month_int = int(month)
                year_int = int(year)
                loop_exit_value = "perfect"

                if year_int > 2100 or year_int < 1950:
                    print('Entered Year is too far from the current period !!!!')
                    print('Enter any year in between 1950 and 2099: ')
                    continue
                if month_int > 12 or month_int <= 0:  # There are only maximum of 12 months
                    print('Invalid month entry... enter again !!!')  # so if the user enter something greater than 12
                    continue
                # ******************************************
                # Finding max number of days in a month
                # ******************************************
                if month_int == 2:
                    if (year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0):
                        max_num_of_days = 29
                    else:
                        max_num_of_days = 28

                elif month_int in [4, 6, 9, 11]:
                    max_num_of_days = 30
                else:
                    max_num_of_days = 31
                # ******************************************
                # Finding max number of days in a month FINISHED
                # ******************************************

                if day_int > max_num_of_days or day_int <= 0:
                    print('Invalid day entry for the month... enter again !!!')
                    continue
                date_to_be_entered = f'{day}/{month}/{year}'
                break
            except ValueError:
                print("invalid date format... enter again !!!")
                continue
    return date_to_be_entered


def positive_float_entry(float_input):  # Positive Float entry function
    loop_exit_value = "value error"
    while loop_exit_value == "value error":
        try:
            user_float_input = float(input(f'Enter {float_input}: '))
            if user_float_input > 0:
                loop_exit_value = "perfect"
            else:
                print(f"invalid {float_input} entry")
                loop_exit_value = "value error"
        except ValueError:
            print(f"invalid {float_input} entry")
            loop_exit_value = "value error"
    return user_float_input


def float_entry(float_input):  # Float entry function
    loop_exit_value = "value error"
    while loop_exit_value == "value error":
        try:
            float_input = float(input(f'Enter {float_input} '))
            return float_input
        except ValueError:
            print(f"invalid {float_input} entry")
            loop_exit_value = "value error"
    return float_input


#  Functions for Delivery buy list
def equity_delivery_buy_entry(symbol, date):
    buy_date = date  # date_entry(buy_date)  # Calling date entry function defined in this codes
    buy_price = "BUY PRICE"
    buy_price = positive_float_entry(buy_price)  # Calling Float entry function defined in this codes
    quantity = "QUANTITY"
    quantity = positive_float_entry(quantity)  # Calling Float entry function defined in this codes
    quantity = int(quantity)  # conversion to integer as Quantity should be integer
    # A list of list for the preparation of Excel or CSV file
    to_be_csv_or_excel = [buy_date, symbol, quantity, buy_price]
    return to_be_csv_or_excel


#  Functions for Delivery sell list
def equity_delivery_sell_entry(symbol, date):
    sell_price = "SELL PRICE"
    sell_price = positive_float_entry(sell_price)  # Calling Float entry function defined in this codes
    sell_date = date  # date_entry(sell_date)
    quantity = "QUANTITY"
    quantity = positive_float_entry(quantity)  # Calling Float entry function defined in this codes
    quantity = int(quantity)  # conversion to integer as Quantity should be integer
    while True:
        dp_charge = input("Dp charge?: y or n ?: ")
        if dp_charge == "y":
            dp_charge = "yes"
            break
        elif dp_charge == "n":
            dp_charge = "BTST"
            break
        else:
            print("Invalid selection on dp charge\n")
    # A list of list for the preparation of Excel or CSV file
    to_be_csv_or_excel = [symbol, quantity, sell_price, sell_date, dp_charge]
    # print(to_be_CSV)
    print(" ")
    return to_be_csv_or_excel


#  Functions for Intraday transaction
def equity_intraday_entry(symbol, date):
    transaction_date = date  # date_entry(transaction_date)  # Calling date entry function defined in this codes
    buy_price = "BUY PRICE"
    buy_price = positive_float_entry(buy_price)  # Calling Float entry function defined in this codes
    quantity = "QUANTITY"
    quantity = positive_float_entry(quantity)  # Calling Float entry function defined in this codes
    quantity = int(quantity)  # conversion to integer as Quantity should be integer
    sell_price = "SELL PRICE"
    sell_price = positive_float_entry(sell_price)  # Calling Float entry function defined in this codes
    # A list of list for the preparation of Excel or CSV file
    to_be_csv_or_excel = [transaction_date, symbol, quantity, buy_price, sell_price]
    # print(to_be_CSV)
    print(" ")
    return to_be_csv_or_excel