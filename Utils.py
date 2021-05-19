def date_entry(date_to_be_entered):  # date entry function
    while True:  # While loop should continue "loop exit value" is equal to "value error"
        try:
            date_format = input(f'Enter {date_to_be_entered} in "dd/mm/yyyy" format: ')
            [day, month, year] = date_format.split("/")
            day = int(day)
            month = int(month)
            year = int(year)

            while year > 2099 or year < 1950:
                print('Entered Year is too far from the current period !!!!')
                year = int(input('Enter any year in between 1950 and 2099: '))
            while month > 12 or month <= 0:  # There are only maximum of 12 months
                print('Invalid month entry !!! ')  # so if the user enter something greater than 12
                month = int(input('enter the month: '))  # it should be shown invalid
            # ******************************************
            # Finding max number of days in a month
            # ******************************************
            if month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    max_num_of_days = 29
                else:
                    max_num_of_days = 28

            elif month in [4, 6, 9, 11]:
                max_num_of_days = 30
            else:
                max_num_of_days = 31
            # ******************************************
            # Finding max number of days in a month FINISHED
            # ******************************************

            while day > max_num_of_days or day <= 0:
                print('Invalid day entry for the month !!!')
                day = int(input('Enter the day: '))
            date_to_be_entered = f'{day}/{month}/{year}'
            break  # To exit the date loop
        except ValueError:
            print("invalid date format..enter again")
    return date_to_be_entered


def positive_float_entry(float_input_name):  # Positive Float entry function
    while True:
        try:
            user_float_input = float(input(f'Enter {float_input_name}: '))
            if user_float_input > 0:
                break  # Loop exit method
            else:
                print(f"invalid {float_input_name} entry")
        except ValueError:
            print(f"invalid {float_input_name} entry")
    return user_float_input


def float_entry(float_input_name):  # Float entry function
    while True:
        try:
            float_input_name = float(input(f'Enter {float_input_name} '))
            break
        except ValueError:
            print(f"invalid {float_input_name} entry")
    return float_input_name


def int_entry(int_input_name):  # Float entry function
    while True:
        try:
            int_input_name = int(input(f'Enter {int_input_name} '))
            break
        except ValueError:
            print(f"invalid {int_input_name} entry")
    return int_input_name


def stock_entry():

    # Headings for CSV or Excel file...remaining list will be appended as on getting more details.
    to_be_csv_or_excel = [["BUY DATE", "SYMBOL", "QUANTITY", "BUY PRICE", "SELL PRICE", "SELL DATE"]]
    loop_exit_value = " "
    # This is for reusing the Code to enter another calculation from last step
    # "Press "e" to exit and "Enter" to do it again"
    while loop_exit_value == " ":
        # User to enter the below details
        print(' ')
        buy_date = "BUY DATE"
        buy_date = date_entry(buy_date)  # Calling date entry function defined in this codes
        symbol = input('Enter SYMBOL: ')
        symbol = symbol.upper()
        buy_price = "BUY PRICE"
        buy_price = positive_float_entry(buy_price)  # Calling Float entry function defined in this codes
        quantity = "QUANTITY"
        quantity = positive_float_entry(quantity)  # Calling Float entry function defined in this codes
        quantity = int(quantity)  # conversion to integer as Quantity should be integer
        sell_price = "SELL PRICE"
        sell_price = positive_float_entry(sell_price)  # Calling Float entry function defined in this codes
        sell_date = "SELL DATE"
        sell_date = date_entry(sell_date)  # Calling date entry function defined in this codes
        # User to enter the below details ***FINISHED****
        # print(' ')
        # input("Press enter to show the details: ")
        # print(' ')
        # Defined variables as brokerage, taxes, other charges...  etc
        intra_day_brokerage_percentage = 0.0003
        intra_day_max_one_side_brokerage = 20

        if buy_date == sell_date:  # Intra day variables
            security_transaction_tax_percentage_buy_side = 0
            security_transaction_tax_percentage_sell_side = 0.00025
            stamp_duty_percentage = 0.00003
            exchange_transaction_charge_percentage = 0.0000325
            variable_for_buy_date = "Transaction date"  # To print "Transaction date" instead of "BUY DATE" for Intra day
            sebi_charge_percentage = 0.0000005
            dp_charge = 0
            gst_percentage = 0.18
            print("This is an Intra Day trade")
        else:  # Delivery variables
            security_transaction_tax_percentage_buy_side = 0.001
            security_transaction_tax_percentage_sell_side = 0.001
            stamp_duty_percentage = 0.00015
            variable_for_buy_date = "BUY DATE"
            exchange_transaction_charge_percentage = 0.0000325
            sebi_charge_percentage = 0.0000005
            dp_charge = 13.5
            gst_percentage = 0.18
            print("This is a Delivery trade ")
        # Defined variables as brokerage, taxes, other charges...  etc FINISHED

        # Turn over calculation
        turn_over = float((buy_price + sell_price) * quantity)
        # Turn over calculation finished

        # Brokerage calculation "intra day" or "delivery"
        if buy_date == sell_date:
            if intra_day_brokerage_percentage * buy_price * quantity > intra_day_max_one_side_brokerage:
                buy_brokerage = intra_day_max_one_side_brokerage
            else:
                buy_brokerage = intra_day_brokerage_percentage * buy_price * quantity
            if intra_day_brokerage_percentage * sell_price * quantity > intra_day_max_one_side_brokerage:
                sell_brokerage = intra_day_max_one_side_brokerage
            else:
                sell_brokerage = intra_day_brokerage_percentage * sell_price * quantity
        else:
            buy_brokerage = 0
            sell_brokerage = 0
        total_brokerage = buy_brokerage + sell_brokerage
        # Brokerage calculation "intra day" or "delivery" FINISHED

        # STT calculation
        security_transaction_tax = (security_transaction_tax_percentage_sell_side * sell_price +
                                    security_transaction_tax_percentage_buy_side * buy_price) * quantity
        # STT calculation FINISHED

        # Exchange transaction charge calculation
        exchange_transaction_charge = exchange_transaction_charge_percentage * turn_over
        # Exchange transaction charge calculation FINISHED

        # SEBI charges calculation
        sebi_charge = sebi_charge_percentage * turn_over
        # SEBI charges calculation FINISHED

        # GST calculation
        gst = gst_percentage * (total_brokerage + exchange_transaction_charge + dp_charge + sebi_charge)
        # GST calculation FINISHED

        # Stamp duty Calculation
        stamp_duty = buy_price * quantity * stamp_duty_percentage
        # 0.003% or Rs 300 per crore on buy-side
        # Stamp duty Calculation FINISHED

        # Total charge calculation
        total_charges = total_brokerage + security_transaction_tax + exchange_transaction_charge + gst + sebi_charge + stamp_duty + dp_charge
        # Total charge calculation FINISHED

        # Net P&L calculation
        net_pnl = quantity * (sell_price - buy_price)
        # Net P&L calculation FINISHED

        # Real P&L calculation
        real_pnl = net_pnl - total_charges
        # Real P&L calculation FINISHED

        # A list of list for the preparation of Excel or CSV file
        to_be_csv_or_excel.append([buy_date, symbol, quantity, buy_price, sell_price, sell_date, net_pnl])  #, real_pnl,
                                   #turn_over, total_brokerage])
        # print(to_be_CSV)
        print(" ")
        loop_exit_value = input('Press space+enter to add more OR press enter to finish')
    return to_be_csv_or_excel

