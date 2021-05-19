from a_Xcel_functions import *

# ********************** Add your excel file path here ********************** #
Common_excel_file_name = "C:\\Users\\dell\\Desktop\\P&L Record May 2021"
Jasi_excel_file_name = "C:\\Users\\dell\\Desktop\\JASI P&L Record May 2021"
individual_excel_file_path = "C:\\Users\\dell\\Desktop\\Stock\\Individual Stock files\\"
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


def adding_intraday_trade(intraday_trade_list):
    intraday_list_of_list = reading_list_from_excel(Common_excel_file_name, sheet_name_for_common_and_jasi,
                                                    intraday_list_row_start, intraday_list_row_ending,
                                                    intraday_list_column_start, intraday_list_column_ending)
    index_to_be_added = intraday_list_of_list.index(intraday_blank_list_format)
    intraday_list_of_list.insert(index_to_be_added, intraday_trade_list)
    write_list_of_list_to_excel(Common_excel_file_name, sheet_name_for_common_and_jasi, intraday_list_row_start,
                                intraday_list_column_start, intraday_list_of_list)


def adding_delivery_buy(delivery_buy_trade_list):
    delivery_buy_list_of_list = reading_list_from_excel(Common_excel_file_name, sheet_name_for_common_and_jasi,
                                                        delivery_list_row_start, delivery_list_row_ending,
                                                        delivery_list_column_start, delivery_list_column_ending)
    index_to_be_added = delivery_buy_list_of_list.index(delivery_blank_list_format)
    delivery_buy_list_of_list.insert(index_to_be_added, delivery_buy_trade_list)
    write_list_of_list_to_excel(Common_excel_file_name, sheet_name_for_common_and_jasi, delivery_list_row_start,
                                delivery_list_column_start, delivery_buy_list_of_list)


def adding_delivery_sell(delivery_sell_trade_list):
    delivery_sell_trade_list1 = list(delivery_sell_trade_list)
    delivery_list_of_list = reading_list_from_excel(Common_excel_file_name, sheet_name_for_common_and_jasi,
                                                        delivery_list_row_start, delivery_list_row_ending,
                                                        delivery_list_column_start, delivery_list_column_ending)

    # To make delivery sell list from delivery_list_of_list
    delivery_sell_list_of_list = []
    for i in range(127):
        delivery_sell_list = []
        for j in range(4, 7):
            delivery_sell_list.append(delivery_list_of_list[i][j])
        delivery_sell_list_of_list.append(delivery_sell_list)
        # Making of delivery sell list of list finished Successfully
    print(delivery_sell_list_of_list)

    # To make "Symbols list for searching" from "delivery_list_of_list"
    symbol_list_in_portfolio = []
    for x in range(127):
        symbol_list_in_portfolio.append(delivery_list_of_list[x][1])
    # print(f' symbols in port folio are {symbol_list_in_portfolio}')
    # Making of "Symbols list for searching" from "delivery_list_of_list" finished Successfully

    # To check the given scrip's index in the "Symbols list for searching"

    # Or to check if it is not available
    try:
        scrip_first_index = symbol_list_in_portfolio.index(delivery_sell_trade_list1[0])
    except ValueError:
        scrip_first_index = 0
        print("The entered scrip is not available in your portfolio")
    # Checking completed successfully

    # To find the Total quantity available
    symbol_list_in_portfolio1 = list(symbol_list_in_portfolio)
    symbol_list_in_portfolio2 = list(symbol_list_in_portfolio)
    total_quantity = 0
    while True:
        try:
            temp_variable_to_find_scrip_last_index = symbol_list_in_portfolio1.index(delivery_sell_trade_list1[0])
            symbol_list_in_portfolio1.pop(temp_variable_to_find_scrip_last_index)
            symbol_list_in_portfolio1.insert(temp_variable_to_find_scrip_last_index, [None])
            if delivery_sell_list_of_list[temp_variable_to_find_scrip_last_index] == [None, None, None]:
                bought_quantity_in_that_line = delivery_list_of_list[temp_variable_to_find_scrip_last_index][2]
                total_quantity += bought_quantity_in_that_line
                scrip_last_index = temp_variable_to_find_scrip_last_index
            else:
                continue
        except ValueError:
            if total_quantity == 0:
                print("The entered scrip is not available in your portfolio")
            else:
                print(f'Total quantiy is {total_quantity}')
            break
        # Finding Total quantity available completed Successfully

    # **************************************************************************************************************
    # ******************************      FINISHED TILL THIS    ****************************************************
    # **************************************************************************************************************

    # To write the quantity to excel and adjust the remaining quantity if any(Below)
    # To insert to the list
    # print("new temp_variable_to_find_scrip_last_index is ", temp_variable_to_find_scrip_last_index)
    # print("new scrip_first_index is ", scrip_first_index)
    remaining_quantity = total_quantity
    quantity_to_be_sold = delivery_sell_trade_list1[1]
    # print("first to_be_sold_quantity is ", quantity_to_be_sold)
    # print(f'first Remaining quantity is {remaining_quantity}')
    # print("first scrip_first_index is ", scrip_first_index)
    # print("first scrip_last_index is ", scrip_last_index)
    print("##################################################################")
#*****************************************************************************************

    if total_quantity > 0:
        if total_quantity < quantity_to_be_sold:
            print("Not enough quantity in your Portfolio")
            to_proceed = input('Press "y" to proceed filling all')
            if to_proceed == "y":
                loopcount = 1
                while True:
                    print("loopcount",loopcount)
                    loopcount += 1
                    try:
                        temp_index = symbol_list_in_portfolio2.index(delivery_sell_trade_list1[0])
                        # print(symbol_list_in_portfolio2)
                        symbol_list_in_portfolio2.pop(temp_index)
                        symbol_list_in_portfolio2.insert(temp_index, [None])
                        # print(symbol_list_in_portfolio2)
                        if delivery_sell_list_of_list[temp_index] == [None, None, None]:
                            print(" BEST CONDITION")
                            print("bought_quantity_in_that_line",loopcount,":", delivery_list_of_list[temp_index][2])
                            bought_quantity_in_that_line = delivery_list_of_list[temp_index][2]
                            print("quantity_to_be_sold is ", quantity_to_be_sold)
                            print(f'first Remaining quantity is {remaining_quantity}')
                            if remaining_quantity == quantity_to_be_sold:
                                print("condition 1 remaining_quantity == quantity_to_be_sold")
                                delivery_sell_list_of_list.pop(temp_index)
                                delivery_sell_list_of_list.insert(temp_index, delivery_sell_trade_list1[2:])
                                remaining_quantity = quantity_to_be_sold - delivery_list_of_list[temp_index][2]
                                quantity_to_be_sold = remaining_quantity
                                continue

                            elif bought_quantity_in_that_line == quantity_to_be_sold:
                                print("condition 2" )
                                delivery_sell_list_of_list.pop(temp_index)
                                delivery_sell_list_of_list.insert(temp_index, delivery_sell_trade_list1[2:])
                                write_list_of_list_to_excel(Common_excel_file_name, sheet_name_for_common_and_jasi,
                                                            delivery_sell_list_row_start,
                                                            delivery_sell_list_column_start, delivery_sell_list_of_list)
                                break

                                # *****************************************************************************************
                                # ***************************MILE STONE *********************************************
                                # *****************************************************************************************

                            elif bought_quantity_in_that_line > quantity_to_be_sold > 0:
                                delivery_sell_list_of_list.pop(temp_index)
                                delivery_sell_list_of_list.insert(temp_index, delivery_sell_trade_list1[2:])
                                delivery_list_of_list[temp_index][2] = bought_quantity_in_that_line - quantity_to_be_sold
                                new_buy_list_to_be_append = list(delivery_list_of_list[temp_index])
                                delivery_list_of_list[temp_index][2] = quantity_to_be_sold
                                delivery_list_of_list.insert(temp_index+1, new_buy_list_to_be_append)
                                write_list_of_list_to_excel(Common_excel_file_name, sheet_name_for_common_and_jasi,
                                                            delivery_list_row_start,
                                                            delivery_list_column_start, delivery_list_of_list)
                                print("condition 3 loop 1 onlyy almost final")
                                write_list_of_list_to_excel(Common_excel_file_name, sheet_name_for_common_and_jasi,
                                                            delivery_sell_list_row_start,
                                                            delivery_sell_list_column_start, delivery_sell_list_of_list)
                                break
                            # *****************************************************************************************
                            # ***************************MILE STONE 2 *********************************************
                            # *****************************************************************************************
                            elif bought_quantity_in_that_line < quantity_to_be_sold:
                                print("Condition4")
                                delivery_sell_list_of_list.pop(temp_index)
                                delivery_sell_list_of_list.insert(temp_index, delivery_sell_trade_list1[2:])
                                quantity_to_be_sold = quantity_to_be_sold - delivery_list_of_list[temp_index][2]
                                remaining_quantity = remaining_quantity - delivery_list_of_list[temp_index][2]
                                continue
                    except ValueError:
                        write_list_of_list_to_excel(Common_excel_file_name, sheet_name_for_common_and_jasi,
                                                    delivery_sell_list_row_start,
                                                    delivery_sell_list_column_start, delivery_sell_list_of_list)
                        print("ValueError")
                        break



#******************************************************************************************************

# intraday_trade_list = ["03/05/2021", "KOPRA", 1, 492.25, 492.90]
# adding_intraday_trade(intraday_trade_list)
# print("First done")
#
# delivery_buy_trade_list = ['22/12/2020', 'TATA', 24, 125.00]
# adding_delivery_buy(delivery_buy_trade_list)
# print("Second done")

delivery_sell_trade_list = ["TATA", 500, 130, "22/12/2020", "yes"]
adding_delivery_sell(delivery_sell_trade_list)
print('Third done')
