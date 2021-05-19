from Xcel_functions import *

# ********************** Add your excel file path here ********************** #
Common_excel_file_name = "C:\\Users\\dell\\Desktop\\P&L Record May 2021"
Jasi_excel_file_name = "C:\\Users\\dell\\Desktop\\JASI P&L Record May 2021"
individual_excel_file_path = "C:\\Users\\dell\\Desktop\\Stock\\Individual Stock files\\"
sheet_name_for_common_and_jasi = "P&L writing"
# ********************** Add your excel file path here ********************** #


def add_data_to_common_excel(file_name, list_to_be_added_to_common_excel, trade_for_common_excel,
                             stock_name_for_common_excel):
    list_to_be_added_to_jasi_excel = list(list_to_be_added_to_common_excel)
    sheet_name = sheet_name_for_common_and_jasi
    if trade_for_common_excel == "intra day":
        row_start_for_reading = 11
        row_ending_for_reading = 67
        column_start_for_reading = 2
        column_ending_for_reading = 6
        blank_list_format = [None, None, None, None, None]
        row_start = iteration_to_find_a_filled_till(file_name, sheet_name, row_start_for_reading,
                                                    row_ending_for_reading, column_start_for_reading,
                                                    column_ending_for_reading, blank_list_format)
        column_start = 2
        writing_list_to_excel(file_name, sheet_name, list_to_be_added_to_common_excel, row_start, column_start)

    elif trade_for_common_excel == "delivery buy":
        row_start_for_reading = 73
        row_ending_for_reading = 200
        column_start_for_reading = 2
        column_ending_for_reading = 8
        blank_list_format = [None, None, None, None, None, None, None]
        row_start = iteration_to_find_a_filled_till(file_name, sheet_name, row_start_for_reading,
                                                    row_ending_for_reading, column_start_for_reading,
                                                    column_ending_for_reading, blank_list_format)
        column_start = 2
        writing_list_to_excel(file_name, sheet_name, list_to_be_added_to_common_excel, row_start, column_start)

    #  *****************************************************************************************************  #
    #  *****************************************Delivery sell Common starting******************************** #
    #  *****************************************************************************************************  #
    elif trade_for_common_excel == "delivery sell":
        #  ************************************************************************************* #
        #  to find total quantity in portfolio (below)
        #  ************************************************************************************* #
        row_ending_for_delivery_iteration = iteration_to_find_a_filled_till(file_name, sheet_name, 73, 200, 2, 8,
                                                                            [None, None, None, None, None, None,
                                                                             None])
        row_start_for_reading = 73
        tot_qty_in_portfolio = 0
        x = 0
        while True:
            if x % 2 != 0:
                print("Processing.....")
            x += 1
            column_start_for_reading = 3
            column_ending_for_reading = 3
            blank_list_format = [stock_name_for_common_excel]
            try:
                row_start = iteration_to_find_a_filled_till(file_name, sheet_name, row_start_for_reading,
                                                            row_ending_for_delivery_iteration,
                                                            column_start_for_reading,
                                                            column_ending_for_reading, blank_list_format)
            except ValueError:
                # print(tot_qty_in_portfolio)
                break
            row_start_for_reloop = row_start + 1
            sell_side_list = reading_list_from_excel(file_name, sheet_name, row_start, row_start, 6, 8)
            if sell_side_list == [[None, None, None]]:  # To check if sell area is blank
                buy_side_list = reading_list_from_excel(file_name, sheet_name, row_start, row_start, 2, 5)
                buy_quantity = buy_side_list[0][2]
                if tot_qty_in_portfolio == 0:
                    row_start_for_reading_for_adding = row_start_for_reloop - 1
                tot_qty_in_portfolio += buy_quantity
                row_start_for_reading = row_start_for_reloop
                if row_start_for_reading < row_ending_for_delivery_iteration:
                    continue
                else:
                    break
            else:
                row_start_for_reading = row_start_for_reloop
        if tot_qty_in_portfolio == 0:
            print("The entered Scrip is not in your portfolio")
        else:
            print(f'Total quantity available in portfolio: {tot_qty_in_portfolio}')
            print("Processing.....")
        # To find total quantity in portfolio (finished)
        #  ************************************************************************************* #
        # to find total quantity in portfolio (finished)
        #  ************************************************************************************* #

        #  ************************************************************************************* #
        # To write the quantity to excel and adjust the remaining quantity if any(Below)
        #  ************************************************************************************* #
        x = 0
        while True:
            if x % 2 == 1:
                print("Processing.....")
            x += 1
            row_ending_for_reading = row_ending_for_delivery_iteration
            column_start_for_reading = 3
            column_ending_for_reading = 3
            blank_list_format = [stock_name_for_common_excel]
            try:
                row_start = iteration_to_find_a_filled_till(file_name, sheet_name, row_start_for_reading_for_adding,
                                                            row_ending_for_reading, column_start_for_reading,
                                                            column_ending_for_reading, blank_list_format)
            except ValueError:
                break
            row_start_for_reloop_reading_for_adding = row_start+1
            buy_side_list = reading_list_from_excel(file_name, sheet_name, row_start, row_start, 2, 5)
            # "buy_side_list" is fetched data from buy area
            # print(f'[[buydate,scrip, buy_quantity, buyprice]] is ?{buy_side_list}')
            [buydate, scrip, buy_quantity, buyprice] = buy_side_list[0]
            # print(f'sell qty is {list_to_be_added[1]}')
            sell_quantity = list_to_be_added_to_common_excel[1]

            if sell_quantity > tot_qty_in_portfolio:  # Main condition 01
                # ************************************
                # print("Main condition 01")
                # ************************************
                print("Not enough quantity available in portfolio")
                if file_name == Jasi_excel_file_name:
                    # ************************************
                    # print("Main condition 01-1")
                    # ************************************
                    sell_full = input('Should we fill it all? press "y" to fill all:')
                    if sell_full == 'y':
                        # ************************************
                        # print("Main condition 01-1-1")
                        # ************************************
                        writing_list_to_excel(file_name, sheet_name, list_to_be_added_to_common_excel[2:5],
                                              row_start, 6)
                        tot_qty_in_portfolio = tot_qty_in_portfolio - buy_quantity
                        list_to_be_added_to_common_excel[1] = sell_quantity - buy_quantity
                        list_to_be_added_to_common_excel[4] = "Sold w others"
                        row_start_for_reading_for_adding = row_start_for_reloop_reading_for_adding
                        continue
                else:
                    # ************************************
                    # print("Main condition 01-1 else")
                    # ************************************
                    break
                # Main condition 01 finished

            elif sell_quantity == tot_qty_in_portfolio:  # Main condition 02
                # ************************************
                # print("Main condition 02")
                # ************************************
                writing_list_to_excel(file_name, sheet_name, list_to_be_added_to_common_excel[2:5], row_start,
                                      6)
                tot_qty_in_portfolio = tot_qty_in_portfolio - buy_quantity
                list_to_be_added_to_common_excel[1] = sell_quantity - buy_quantity
                list_to_be_added_to_common_excel[4] = "Sold w others"
                row_start_for_reading_for_adding = row_start_for_reloop_reading_for_adding
                continue
                # Main condition 02 finished program will end when "adding finished"

            elif sell_quantity < tot_qty_in_portfolio and sell_quantity != 0:  # Main condition 03
                # ************************************
                # print("Main condition 03")
                # ************************************
                if sell_quantity < buy_quantity:
                    # ************************************
                    # print("Main condition 03-1")
                    # ************************************
                    qty_on_buy_list_to_be_added = buy_quantity - sell_quantity
                    # print(f"to be added {qty_on_buy_list_to_be_added}")
                    writing_list_to_excel(file_name, sheet_name, list_to_be_added_to_common_excel[2:5],
                                          row_start, 6)
                    # to make buy quantity as  sell quantity (below)
                    writing_list_to_excel(file_name, sheet_name, [sell_quantity], row_start, 4)
                    # to_insert_row_copy_n_move_down()
                    if sell_quantity != 0:
                        # ************************************
                        # print("Main condition 03-1-1") LAST ADJUSTMENT
                        # ************************************
                        print("Processing.....almost complete..")
                        to_insert_row_copy_n_move_down(file_name, sheet_name, row_start + 1, 198, 2, 8)
                        # new delivery buy to be added "qty_on_buy_list_to_be_added"
                        new_row_start = row_start + 1
                        writing_list_to_excel(file_name, sheet_name,
                                              [buydate, list_to_be_added_to_common_excel[0],
                                               qty_on_buy_list_to_be_added,
                                               buyprice], new_row_start, 2)
                        break
                    else:
                        # ************************************
                        # print("Main condition 03-1-2")
                        # ************************************
                        break
                else:
                    # ************************************
                    # print("Main condition 03-2")
                    # ************************************
                    writing_list_to_excel(file_name, sheet_name, list_to_be_added_to_common_excel[2:5],
                                          row_start, 6)
                    tot_qty_in_portfolio = tot_qty_in_portfolio - buy_quantity
                    list_to_be_added_to_common_excel[1] = sell_quantity - buy_quantity
                    list_to_be_added_to_common_excel[4] = "Sold w others"
                    if sell_quantity == buy_quantity:
                        break
                    else:
                        row_start_for_reading_for_adding = row_start_for_reloop_reading_for_adding
                        continue
    return list_to_be_added_to_jasi_excel

    #  *****************************************************************************************************  #
    #  ***************************************** Delivery sell finished ************************************* #
    #  *****************************************************************************************************  #


def to_add_to_common_and_to_add_jasi(stock_name_to_common, list_to_be_added_to_common,
                                     trade_to_common_excel):
    file_name = Common_excel_file_name
    if True:
        if file_name != Jasi_excel_file_name and file_name == Common_excel_file_name:
            list_to_be_added_to_jasi_excel = add_data_to_common_excel(file_name, list_to_be_added_to_common,
                                                                      trade_to_common_excel, stock_name_to_common)

            if file_name == Jasi_excel_file_name:
                pass
            else:
                to_jasi = input("To be added to jasi's file also?: press 'y':")
                if to_jasi == "y":
                    print("Processing.....")
                    file_name = Jasi_excel_file_name
                    list_to_be_added_to_common = list_to_be_added_to_jasi_excel
                    add_data_to_common_excel(file_name, list_to_be_added_to_common, trade_to_common_excel,
                                             stock_name_to_common)


#  **************** THE END ****************  #

#  Test block************************
file_name = "C:\\Users\\dell\\Desktop\\P&L Record May 2021"
list_to_be_added_to_common_excel = ["TATA", 495, 150, "test12/12", "BTST"]
trade_for_common_excel = "delivery sell"
stock_name_for_common_excel = "TATA"

add_data_to_common_excel(file_name, list_to_be_added_to_common_excel, trade_for_common_excel,
                         stock_name_for_common_excel)
