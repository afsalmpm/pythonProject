def date_entry(date_to_be_entered):  # date entry function
    loop_exit_value = "value error"  # While loop should continue "loop exit value" is equal to "value error"
    while loop_exit_value == "value error":  # While loop should continue "loop exit value" is equal to "value error"
        try:
            date_format = input(f'Enter {date_to_be_entered} in "dd/mm/yyyy" format: ')
            [day, month, year] = date_format.split("/")
            day = int(day)
            month = int(month)
            year = int(year)
            loop_exit_value = "perfect"

            while year > 2099 or year < 1950:
                print('Entered Year is too far from the current period !!!!')
                year = int(input('Enter any year in between 1950 and 2099: '))
            while month > 12 or month <= 0:  # There are only maximum of 12 months
                print('Invalid month entry !!! ')  # so if the user enter something greater than 12
                month = int(input('enter the month: '))  # it should be shown invalid
            # **********************************
            # Finding max number of days in a month
            # **********************************
            # 28 days for FEB in normal year and 29 days in leap year FEB (FEB 02)
            # 30 days months are (APRIL 04), (JUNE 06), (SEPTEMBER 09), (NOVEMBER 11)
            # 31 days months are (JAN 01), (MARCH 03), (MAY 05), (JULY 07), (AUGUST 08), (OCTOBER 10), (DECEMBER 12)
            # **********************************
            # Leap year condition below
            # **********************************
            # Every year that is exactly divisible by four is a leap year, except for years that are exactly
            # divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
            # For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are

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

        except ValueError:
            print("invalid date format..enter again")
            loop_exit_value = "value error"
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


# ***********The main code starts from the next line************ #

to_be_CSV = [["BUY DATE", "SYMBOL", "QUANTITY", "BUY PRICE", "SELL PRICE", "SELL DATE",]]
x = ' '  # This is for reusing the Code to enter another calculation from last step "Press "SPACE+ENTER" to do it again"
while x == ' ':
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
    print(' ')
    input("Press enter to show the details: ")
    print(' ')
    # Defined variables as brokerage, taxes, other charges...  etc
    Intra_day_brokerage_percentage = 0.0003
    Intra_day_max_one_side_brokerage = 20

    if buy_date == sell_date:  # Intra day variables
        Security_transaction_tax_percentage_buy_side = 0
        Security_transaction_tax_percentage_sell_side = 0.00025
        Stamp_duty_percentage = 0.00003
        Exchange_transaction_charge_percentage = 0.0000325
        variable_for_buy_date = "Transaction date"  # To print "Transaction date" instead of "BUY DATE" for Intra day
        SEBI_charge_percentage = 0.0000005
        DP_Charge = 0
        Gst_percentage = 0.18
        print("This is an Intra Day trade")
    else:  # Delivery variables
        Security_transaction_tax_percentage_buy_side = 0.001
        Security_transaction_tax_percentage_sell_side = 0.001
        Stamp_duty_percentage = 0.00015
        variable_for_buy_date = "BUY DATE"
        Exchange_transaction_charge_percentage = 0.0000325
        SEBI_charge_percentage = 0.0000005
        DP_Charge = 13.5
        Gst_percentage = 0.18
        print("This is a Delivery trade ")
    # Defined variables as brokerage, taxes, other charges...  etc FINISHED

    # Turn over calculation
    turn_over = float((buy_price + sell_price) * quantity)
    # Turn over calculation finished

    # Brokerage calculation "intra day" or "delivery"
    if buy_date == sell_date:
        if Intra_day_brokerage_percentage * buy_price * quantity > Intra_day_max_one_side_brokerage:
            buyBrokerage = Intra_day_max_one_side_brokerage
        else:
            buyBrokerage = Intra_day_brokerage_percentage * buy_price * quantity
        if Intra_day_brokerage_percentage * sell_price * quantity > Intra_day_max_one_side_brokerage:
            sellBrokerage = Intra_day_max_one_side_brokerage
        else:
            sellBrokerage = Intra_day_brokerage_percentage * sell_price * quantity
    else:
        buyBrokerage = 0
        sellBrokerage = 0
    totalBrokerage = buyBrokerage + sellBrokerage
    # Brokerage calculation "intra day" or "delivery" FINISHED

    # STT calculation
    Security_transaction_tax = (Security_transaction_tax_percentage_sell_side * sell_price +
                                Security_transaction_tax_percentage_buy_side * buy_price) * quantity
    # STT calculation FINISHED

    # Exchange transaction charge calculation
    Exchange_transaction_charge = Exchange_transaction_charge_percentage * turn_over
    # Exchange transaction charge calculation FINISHED

    # SEBI charges calculation
    SEBI_charge = SEBI_charge_percentage * turn_over
    # SEBI charges calculation FINISHED

    # GST calculation
    GST = Gst_percentage * (totalBrokerage + Exchange_transaction_charge + DP_Charge + SEBI_charge)
    # GST calculation FINISHED

    # Stamp duty Calculation
    Stamp_duty = buy_price * quantity * Stamp_duty_percentage
    # 0.003% or Rs 300 per crore on buy-side
    # Stamp duty Calculation FINISHED

    # Total charge calculation
    Total_charges = totalBrokerage + Security_transaction_tax + Exchange_transaction_charge + GST + SEBI_charge + Stamp_duty + DP_Charge
    # Total charge calculation FINISHED

    # Net P&L calculation
    net_PnL = quantity * (sell_price - buy_price)
    # Net P&L calculation FINISHED

    # Real P&L calculation
    Real_PnL = net_PnL - Total_charges
    # Real P&L calculation FINISHED

    # Printing out of user entered details
    print(' ')
    print(f' {variable_for_buy_date}: {buy_date}')
    print(f' SYMBOL: {symbol}')
    print(f' BUY PRICE: {buy_price}')
    print(f' QUANTITY: {quantity}')
    print(f' SELL PRICE: {sell_price}')
    if buy_date != sell_date:  # Print SELL DATE only for Delivery.
        print(f' SELL DATE: {sell_date}')
    print(' ')
    # Printing out of user entered details FINISHED

    # Printing calculated details
    print(f' TURN OVER: {turn_over}')
    print(f' Total Brokerage: {totalBrokerage}')
    print(f' DP Charge: {DP_Charge}')
    print(f' STT: {Security_transaction_tax}')
    print(f' ExcTraCharge: {Exchange_transaction_charge}')
    print(f' SEBI charges: {SEBI_charge}')
    print(f' Total GST: {GST}')
    print(f' Stamp duty: {Stamp_duty}')
    print(f' Total Charges: {Total_charges}')
    print(f' Net P&L: {net_PnL}')
    print(f' Real P&L: {Real_PnL}')

    to_be_CSV.append([buy_date, symbol, quantity, buy_price, sell_price, sell_date])
    # print([buy_date,buy_price,quantity,sell_price,sell_date,totalBrokerage])
    print(to_be_CSV)

    print(" ")
    x = input(' Press "SPACE+ENTER" to do it again or press "ENTER" twice to exit ')

import csv

# data to be written row-wise in csv fil
data = to_be_CSV

# opening the csv file in 'w+' mode
file = open('April P&L.csv', 'w+', newline='')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(data)
