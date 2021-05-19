# Defined variables as brokerage taxes etc
Intra_day_brokerage_percentage = 0.0003
Intra_day_max_one_side_brokerage = 20
Security_transaction_tax_percentage = 0.00025  # Sell side only
Exchange_transaction_charge_percentage = 0.0000325
Gst_percentage = 0.18
SEBI_charge_percentage = 0.0000005
Stamp_duty_percentage = 0.00003


def date_entry(date):  # date entry function
    loop_exit_value = "value error"
    while loop_exit_value == "value error":
        try:
            date_format = input(f'Enter {date} in "dd/mm/yyyy" format ')
            [day, month, year] = date_format.split("/")
            day = int(day)
            month = int(month)
            year = int(year)
            loop_exit_value = "perfect"
            while day > 31:  # Maximum number of days in any month is less than 31
                print('Invalid day entry')
                day = int(input('enter the day '))
            while month > 12:  # As the case of date there is only maximum of 12 months
                print('Invalid month entry')  # so if the user enter something greater than 12
                month = int(input('enter the month '))  # it should be shown invalid
            while year > 2050 or year < 1950:
                print('Year is too far away from the current era')
                year = int(input('enter the year in between 1950 and 2050 '))
            # print(' ')
            date = f'{day}/{month}/{year}'
            # print(f'Date is {day}/{month}/{year}')
        except ValueError:
            print("invalid date format..enter again")
            loop_exit_value = "value error"
    return date


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


Transaction_Date = "Transaction DATE"
Transaction_Date = date_entry(Transaction_Date)
symbol = input('Enter SYMBOL ')
symbol = symbol.upper()
buyPrice = "BUY PRICE"
buyPrice = float_entry(buyPrice)
quantity = "QUANTITY"
quantity = float_entry(quantity)
quantity = int(quantity)
sellPrice = "SELL PRICE"
sellPrice = float_entry(sellPrice)
# sellDate = "SELL DATE"
# sellDate = date_entry(sellDate)
print(' ')
input("Press enter to show the details")
print(' ')
print(f' Transaction date: {Transaction_Date}')
print(f' SYMBOL : {symbol}')
print(f' BUY PRICE : {buyPrice}')
print(f' QUANTITY : {quantity}')
print(f' SELL PRICE : {sellPrice}')

# Turn over calculation
turn_over = float((buyPrice + sellPrice) * quantity)
print(f' TURN OVER : {turn_over}')

# Intra day brokerage calculation
if Intra_day_brokerage_percentage * buyPrice * quantity > Intra_day_max_one_side_brokerage:
    buyBrokerage = Intra_day_max_one_side_brokerage
else:
    buyBrokerage = Intra_day_brokerage_percentage * buyPrice * quantity
if Intra_day_brokerage_percentage * sellPrice * quantity > Intra_day_max_one_side_brokerage:
    sellBrokerage = Intra_day_max_one_side_brokerage
else:
    sellBrokerage = Intra_day_brokerage_percentage * sellPrice * quantity
totalBrokerage = buyBrokerage + sellBrokerage
print(f' Total Brokerage : {totalBrokerage}')
#   =(IF(0.0003*D11*E11>20,20,(0.0003*D11*E11 )))+(IF(0.0003*D11*F11>20,20,(0.0003*D11*F11 )))                    \
# +N(" Bokerage = [IF 0.03% of (Qty*Buy price) is greater than 20 then 20 else 0.03% of (QTY*Buy price)] + [IF 0.03% of (QTY*Sell price is greater than 20 then 20 else (0.03% of (QTY*Sell price) ] ")

# Intra day STT calculation
Security_transaction_tax = Security_transaction_tax_percentage * sellPrice * quantity
print(f' STT : {Security_transaction_tax}')
# =0.00025*(D11*F11)            +N("  0.025% on the sell side ")

# Exchange transaction charge calculation
Exchange_transaction_charge = Exchange_transaction_charge_percentage * turn_over
print(f' ExcTraCharge : {Exchange_transaction_charge}')
# =0.0000325*J11

# GST calculation
GST = Gst_percentage * (totalBrokerage + Exchange_transaction_charge)
print(f' Total GST : {GST}')
# =0.18*(T11+V11)

# SEBI charges calculation
SEBI_charge = SEBI_charge_percentage * turn_over
print(f' SEBI charges : {GST}')
# =0.0000005*J11

# Stamp duty Calculation
Stamp_duty = buyPrice * Stamp_duty_percentage
print(f' Stamp duty : {Stamp_duty}')
# 0.003% or Rs 300 per crore on buy-side

# Total charge calculation
Total_charges = totalBrokerage + Security_transaction_tax + Exchange_transaction_charge + GST + SEBI_charge + Stamp_duty
print(f' Total Charges : {Total_charges}')

# Net P&L calculation
net_P = quantity * (sellPrice - buyPrice)
print(f' Net P&L : {net_P}')

# Real P&L calculation
Real_P = net_P - Total_charges
print(f' Real P&L : {Real_P}')
