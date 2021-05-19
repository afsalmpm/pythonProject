from a_Xcel_functions import *
import Xcel_files
# ********************** Add your excel file path here ********************** #
Common_excel_file_name = f"{Xcel_files.file_path}{Xcel_files.file1_name}"
Jasi_excel_file_name = f"{Xcel_files.file_path}{Xcel_files.file2_name}"
sheet_name_for_common_and_jasi = "P&L writing"
# ********************** Add your excel file path here ********************** #
# For reading & writing intraday list from & to excel file
intraday_list_row_start = 11
intraday_list_row_ending = 67
intraday_list_column_start = 2
intraday_list_column_ending = 6
intraday_blank_list_format = [None, None, None, None, None]

# For reading & writing delivery buy list from excel file
delivery_list_row_start = 72
delivery_list_row_ending = 200
delivery_list_column_start = 2
delivery_list_column_ending = 8
delivery_blank_list_format = [None, None, None, None, None, None, None]

# For reading & writing delivery sell list from excel file
delivery_sell_list_row_start = 72
delivery_sell_list_row_ending = 200
delivery_sell_list_column_start = 6
delivery_sell_list_column_ending = 8
delivery_sell_blank_list_format = [None, None, None]


def adding_intraday_trade(excel_filename, intraday_trade_list):
    intraday_list_of_list = reading_list_from_excel(excel_filename, sheet_name_for_common_and_jasi,
                                                    intraday_list_row_start, intraday_list_row_ending,
                                                    intraday_list_column_start, intraday_list_column_ending)
    index_to_be_added = intraday_list_of_list.index(intraday_blank_list_format)
    intraday_list_of_list.insert(index_to_be_added, intraday_trade_list)
    over_write_list_of_list_to_excel(excel_filename, sheet_name_for_common_and_jasi, intraday_list_row_start,
                                     intraday_list_column_start, intraday_list_of_list)


def adding_delivery_buy(excel_filename, delivery_buy_trade_list):
    delivery_buy_list_of_list = reading_list_from_excel(excel_filename, sheet_name_for_common_and_jasi,
                                                        delivery_list_row_start, delivery_list_row_ending,
                                                        delivery_list_column_start, delivery_list_column_ending)
    index_to_be_added = delivery_buy_list_of_list.index(delivery_blank_list_format)
    delivery_buy_list_of_list.insert(index_to_be_added, delivery_buy_trade_list)
    over_write_list_of_list_to_excel(excel_filename, sheet_name_for_common_and_jasi, delivery_list_row_start,
                                     delivery_list_column_start, delivery_buy_list_of_list)


def adding_delivery_sell(excel_filename, delivery_sell_trade_list):
    x_delivery_sell_trade_list = list(delivery_sell_trade_list)
    delivery_list_of_list = reading_list_from_excel(excel_filename, sheet_name_for_common_and_jasi,
                                                    delivery_list_row_start, delivery_list_row_ending,
                                                    delivery_list_column_start, delivery_list_column_ending)

    # **************************************************
    # To make delivery sell list from delivery_list_of_list
    delivery_sell_list_of_list = []
    for i in range(127):
        delivery_sell_list = []
        for j in range(4, 7):
            delivery_sell_list.append(delivery_list_of_list[i][j])
        delivery_sell_list_of_list.append(delivery_sell_list)
    # print(delivery_sell_list_of_list)
    # Making of delivery sell list of list finished Successfully
    # **************************************************
    x_delivery_sell_list_of_list = list(delivery_sell_list_of_list)

    # ****************************************************************
    # To make "Symbols list for searching" from "delivery_list_of_list"
    symbol_list_in_portfolio = []
    for x in range(127):
        symbol_list_in_portfolio.append(delivery_list_of_list[x][1])
    # print(f' symbols in port folio are {symbol_list_in_portfolio}')
    # Making of "Symbols list for searching" from "delivery_list_of_list" finished Successfully
    # *****************************************************************

    # *****************************************************************
    # To check the given scrip's index in the "Symbols list for searching"
    # Or to check if it is not available
    try:
        # print(x_delivery_sell_trade_list[0])
        scrip_first_index = symbol_list_in_portfolio.index(x_delivery_sell_trade_list[0])
    except ValueError:
        scrip_first_index = 0
        print("The entered scrip is not available in your portfolio")
    # Checking completed successfully
    # ******************************************************************

    # ******************************************************************
    # To find the Total quantity available
    x_symbol_list_in_portfolio = list(symbol_list_in_portfolio)
    y_symbol_list_in_portfolio = list(symbol_list_in_portfolio)
    total_quantity = 0
    if scrip_first_index != 0:
        while True:
            try:
                temp_variable_to_find_scrip_last_index = x_symbol_list_in_portfolio.index(x_delivery_sell_trade_list[0])
                x_symbol_list_in_portfolio.pop(temp_variable_to_find_scrip_last_index)
                x_symbol_list_in_portfolio.insert(temp_variable_to_find_scrip_last_index, [None])
                if x_delivery_sell_list_of_list[temp_variable_to_find_scrip_last_index] == [None, None, None]:
                    bought_quantity_in_that_line = delivery_list_of_list[temp_variable_to_find_scrip_last_index][2]
                    total_quantity += bought_quantity_in_that_line
                else:
                    continue
            except ValueError:
                if total_quantity == 0:
                    print("The entered scrip is not available in your portfolio")
                else:
                    print(f'Total quantiy is {total_quantity}')
                break
            # Finding Total quantity available completed Successfully
            # *******************************************************************

    # *******************************************************************
    # To ADD SELL ENTRY LAST BUT LONG STEP BELOW ************************
    # *******************************************************************

    remaining_quantity = total_quantity
    quantity_to_be_sold = x_delivery_sell_trade_list[1]
    if total_quantity > 0:
        to_proceed = "y"
        if total_quantity < quantity_to_be_sold:
            print("Not enough quantity available in your Portfolio")
            to_proceed = input('To proceed filling all, Press "y": ')
            quantity_to_be_sold = total_quantity
        if to_proceed == "y":
            loopcount = 1
            while True:
                # print("loopcount",loopcount)
                loopcount += 1
                try:
                    temp_index = y_symbol_list_in_portfolio.index(x_delivery_sell_trade_list[0])
                    # print(symbol_list_in_portfolio2)
                    y_symbol_list_in_portfolio.pop(temp_index)
                    y_symbol_list_in_portfolio.insert(temp_index, [None])
                    # print(symbol_list_in_portfolio2)
                    if x_delivery_sell_list_of_list[temp_index] == [None, None, None]:
                        # ********************************
                        # print(" MUST CONDITION")  # ******
                        # ********************************
                        bought_quantity_in_that_line = delivery_list_of_list[temp_index][2]
                        # print("bought_quantity_in_that_line",loopcount,":", delivery_list_of_list[temp_index][2])
                        # print("quantity_to_be_sold is ", quantity_to_be_sold)
                        # print(f'first Remaining quantity is {remaining_quantity}')
                        if total_quantity == quantity_to_be_sold:
                            # ********************************
                            # print("condition 1: total_quantity == quantity_to_be_sold")
                            # ********************************
                            x_delivery_sell_list_of_list.pop(temp_index)
                            x_delivery_sell_list_of_list.insert(temp_index, x_delivery_sell_trade_list[2:])
                            remaining_quantity = quantity_to_be_sold - delivery_list_of_list[temp_index][2]
                            quantity_to_be_sold = remaining_quantity
                            if x_delivery_sell_trade_list[4] == "yes":
                                x_delivery_sell_trade_list[4] = "Sold W others"
                            continue

                        elif bought_quantity_in_that_line == quantity_to_be_sold:
                            # ********************************
                            # print("condition 2: bought_quantity_in_that_line == quantity_to_be_sold")
                            # ********************************
                            x_delivery_sell_list_of_list.pop(temp_index)
                            x_delivery_sell_list_of_list.insert(temp_index, x_delivery_sell_trade_list[2:])
                            # print("condition 2: Writing delivery_sell_list_of_list")
                            over_write_list_of_list_to_excel(excel_filename, sheet_name_for_common_and_jasi,
                                                             delivery_sell_list_row_start,
                                                             delivery_sell_list_column_start, x_delivery_sell_list_of_list)
                            break

                        elif bought_quantity_in_that_line > quantity_to_be_sold > 0:
                            # ********************************
                            # print("condition 3: bought_quantity_in_that_line > quantity_to_be_sold > 0")
                            # ********************************
                            x_delivery_sell_list_of_list.insert(temp_index, x_delivery_sell_trade_list[2:])
                            delivery_list_of_list[temp_index][2] = bought_quantity_in_that_line - quantity_to_be_sold
                            new_buy_list_to_be_inserted = list(delivery_list_of_list[temp_index])
                            delivery_list_of_list[temp_index][2] = quantity_to_be_sold
                            delivery_list_of_list.insert(temp_index + 1, new_buy_list_to_be_inserted)

                            # To combine delivery_list_of_list and x_delivery_sell_list_of_list below
                            for a in range(127):
                                delivery_list_of_list[a][4:] = x_delivery_sell_list_of_list[a]

                            # To reaplace all None to "" below
                            list_of_list = []
                            for i in delivery_list_of_list:
                                listt = []
                                for j in i:
                                    if j is None:
                                        listt.append("")
                                    else:
                                        listt.append(j)
                                list_of_list.append(listt)
                                delivery_list_of_list = list_of_list
                                # print("condition 3 last step: Writing delivery_list_of_list")
                            over_write_list_of_list_to_excel(excel_filename, sheet_name_for_common_and_jasi,
                                                             delivery_list_row_start,
                                                             delivery_list_column_start, delivery_list_of_list)
                            # *************************************************
                            # print("condition 3: almost final")
                            # *************************************************

                            break
                        elif bought_quantity_in_that_line < quantity_to_be_sold:
                            # **************************************************
                            # print("Condition 4: bought_quantity_in_that_line < quantity_to_be_sold")
                            # **************************************************
                            x_delivery_sell_list_of_list.pop(temp_index)
                            x_delivery_sell_list_of_list.insert(temp_index, x_delivery_sell_trade_list[2:])
                            quantity_to_be_sold = quantity_to_be_sold - delivery_list_of_list[temp_index][2]
                            remaining_quantity = remaining_quantity - delivery_list_of_list[temp_index][2]
                            if x_delivery_sell_trade_list[4] == "yes":
                                x_delivery_sell_trade_list[4] = "Sold W others"
                            continue

                except ValueError:
                    # print("condition 1 & 4 : Writing delivery_sell_list_of_list")
                    over_write_list_of_list_to_excel(excel_filename, sheet_name_for_common_and_jasi,
                                                     delivery_sell_list_row_start,
                                                     delivery_sell_list_column_start, x_delivery_sell_list_of_list)
                    # print("Finished Successfully")
                    # print("ValueError")
                    break
                    # *******************************************************************
                    # To ADD SELL ENTRY LAST BUT LONG STEP ******FINISHED ***************
                    # *******************************************************************


def to_add_to_common_and_to_add_jasi(list_to_be_added, trade):
    file_name = Common_excel_file_name
    if True:
        if file_name != Jasi_excel_file_name and file_name == Common_excel_file_name:
            if trade == "intra day":
                adding_intraday_trade(file_name, list_to_be_added)
            elif trade == "delivery buy":
                adding_delivery_buy(file_name, list_to_be_added)
            elif trade == "delivery sell":
                adding_delivery_sell(file_name, list_to_be_added)

            if file_name == Jasi_excel_file_name:
                pass
            else:
                to_jasi = input("To be added to jasi's file also?: press 'y':")
                if to_jasi == "y":
                    print("Processing.....")
                    file_name = Jasi_excel_file_name
                    if trade == "intra day":
                        adding_intraday_trade(file_name, list_to_be_added)
                    elif trade == "delivery buy":
                        adding_delivery_buy(file_name, list_to_be_added)
                    elif trade == "delivery sell":
                        adding_delivery_sell(file_name, list_to_be_added)

# ******************************************************************************************************
# ************************************** END OF CODE ***************************************************
# ******************************************************************************************************

# ******************************************************************************************************
# *********************************TEST CODES BELOW  ***************************************************
# ******************************************************************************************************

# intraday_trade_list = ["03/05/2021", "KOPRA", 1, 492.25, 492.90]
# adding_intraday_trade(Common_excel_file_name, intraday_trade_list)
# print("First done")

# delivery_buy_trade_list = [Common_excel_file_name, '22/12/2020', 'TATA', 24, 125.00]
# adding_delivery_buy(Common_excel_file_name, delivery_buy_trade_list)
# print("Second done")


# delivery_sell_trade_list = ["TATA", 95, 130, "22/12/2020", "yes"]
# delivery_sell_trade_list[1] = int(input("quantity? :"))
# to_add_to_common_and_to_add_jasi(delivery_sell_trade_list, "delivery sell")
# print('Third done')
# #
# # if trade == "intra day":
# #     adding_intraday_trade(file_name, list_to_be_added)
# # elif trade == "delivery buy":
# #     adding_delivery_buy(file_name, list_to_be_added)
# # elif trade == "delivery sell":
# #     adding_delivery_sell(file_name, list_to_be_added)
